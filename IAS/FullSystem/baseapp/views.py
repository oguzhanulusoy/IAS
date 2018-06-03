from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import UpdateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from CampusSystem.settings import EMAIL_HOST_USER as sender
from django.template.defaulttags import register

import datetime
import random
import threading
from .forms import *
from .models import *
from .lists import *

# Ömer Berkhan - Burak Sağlam


def index(request):
    if request.user.is_authenticated:
        if request.user.get_type() is Student:
            return HttpResponseRedirect('/student')
        elif request.user.get_type() is AcademicStaff:
            academic_staff = request.user.staff.academicstaff
        elif request.user.get_type() is Staff:
            staff = request.user.staff
    else:
        return HttpResponseRedirect('/login')
    form = LoginForm()
    return render(request, 'home.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                context = {'error': 'Incorrect ID or Password', 'form': form}
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    return render(request, 'user/profile.html')


def student_home_view(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        next_lecture = student.get_next_lecture()

        notifications = []
        if student.hold_state:
            notifications.append('You have registration hold!')

        reg_statue = 0
        if student.hold_state:
            reg_statue = 1  # Hold
        elif student.reg_open_statue:
            reg_statue = 3  # Registration process continues
        elif not student.reg_open_statue and not student.approval_statue:
            reg_statue = 2  # Waiting for approve

        context = {'next_lecture': next_lecture, 'reg_statue': reg_statue, 'notifications': notifications}
        return render(request, 'home.html', context)
    return HttpResponseRedirect('/')


def student_ccr_view(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student:
            ccr = student.get_curriculum()
            comp_courses = student.get_completed_courses()
            context = {'courses': ccr, 'comp_courses': comp_courses}
            return render(request, 'student/ccr.html', context)
    return HttpResponseRedirect('/')

def student_ccr_external_view(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student:
            ccr = student.get_curriculum()
            comp_courses = student.get_completed_courses()
            context = {'courses': ccr, 'comp_courses': comp_courses}
            return render(request, 'student/ccr_external.html', context)
    return HttpResponseRedirect('/')

def student_schedule_view(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student:
            schedule = student.get_schedule()
            context = {'dict': schedule, 'slots': SLOTS}
            return render(request, 'student/schedule.html', context)
    return HttpResponseRedirect('/')


def student_transcript_view(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student:
            comp_courses = student.get_completed_courses()

            semesters = {}

            for comp_course in comp_courses:
                semester = str(comp_course.act_course.year) + ' ' + str(comp_course.act_course.semester)

                if semester not in semesters.keys():
                    semesters[semester] = []
                semesters[semester].append(comp_course)

            semester_info = {}
            for semester, courses in semesters.items():
                credits_attempted = 0
                credits_comp = 0
                points_earned = 0

                for course in courses:
                    credits_attempted += int(course.credit)

                    points_earned += (grade_point(course.grade) * course.credit)

                    if grade_point(course.grade) >= 2:
                        credits_comp += int(course.credit)

                spa = round(points_earned/credits_attempted, 2)

                sem_status = semester_status(spa)

                semester_info[semester] = {'credits_attempted': credits_attempted,
                                           'credits_comp': credits_comp,
                                           'points_earned': points_earned,
                                           'spa': spa,
                                           'semester_status': sem_status}

            return render(request, 'student/transcript.html', {'semesters': semesters, 'semester_info': semester_info})
    return HttpResponseRedirect('/')


def personal_information_view(request):
    if request.user.is_authenticated:
        try:
            personal_information = PersonalInformation.objects.get(user=request.user)
            form = PersonalInformationForm(initial={
                'id_number': personal_information.id_number,
                'gender': personal_information.gender,
                'nationality': personal_information.nationality,
                'birth_date': personal_information.birth_date,
                'birth_place': personal_information.birth_place,
                'marital_status': personal_information.marital_status,
                'religion': personal_information.religion,
                'blood_type': personal_information.blood_type,
                'province': personal_information.province,
                'district': personal_information.district,
                'village': personal_information.village,
                'registration_no': personal_information.registration_no,
                'family_no': personal_information.family_no,
                'order_no': personal_information.order_no,
                'mother_name': personal_information.mother_name,
                'father_name': personal_information.father_name
            })
        except ObjectDoesNotExist:
            form = PersonalInformationForm()

        return render(request, 'user/information.html', {'form': form})
    return HttpResponseRedirect('/')


def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            tc = form.cleaned_data['tc']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            birthday = form.cleaned_data['birthday']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            degree = form.cleaned_data['degree']
            university = form.cleaned_data['university']
            gpa = form.cleaned_data['gpa']
            ales = form.cleaned_data['ales']
            yds = form.cleaned_data['yds']
            programs = form.cleaned_data['program']

            if Visitor.objects.filter(tc=tc):
                form.add_error('tc', 'This TC number is in use')
                return render(request, 'application/index.html', {'form': form})

            if User.objects.filter(email=email):
                form.add_error('email', 'This email address is in use')
                return render(request, 'application/index.html', {'form': form})

            if not programs:
                form.add_error('program', 'You have to select at least one program')
                return render(request, 'application/index.html', {'form': form})

            password = generate_password()
            user = User.create(first_name, last_name, email, phone_number, password)
            user.save()
            user.username = 'visitor_' + str(user.id)
            user.save()

            visitor = Visitor.create(user, tc, birthday, gender, address, city, degree, university, gpa, ales, yds)
            visitor.save()

            for program in programs:
                applied_programs = VisitorProgram.create(visitor, program)
                applied_programs.save()

            SendMail(password, email).start()

            return render(request, 'application/success_page.html', {'form': form})
        else:
            print(form.errors)
            return render(request, 'application/index.html', {'form': form})
    else:
        form = ApplicationForm()
        return render(request, 'application/index.html', {'form': form})


def student_register_course_view(request, selected_course_id=None):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student.can_edit_program():

            st_taken_credit = student.get_taken_credit()
            st_max_credit = student.get_maximum_credit()
            warnings = []
            if st_taken_credit > st_max_credit:
                warnings.append('You have exceeded the allowed credit limit. You can get a maximum of '
                                + str(st_max_credit) + ' credits')

            taken_courses = student.get_taken_courses()
            ccr = student.get_curriculum()

            ccr_course = None
            offered_courses = None
            if selected_course_id is not None:
                try:
                    ccr_course = CcrCourse.objects.get(pk=selected_course_id)
                    offered_courses = ccr_course.get_offered_courses()
                except CcrCourse.DoesNotExist:
                    return redirect('student_register_course')

            try:
                error = request.session['select_course_error']
                del request.session['select_course_error']
            except KeyError:
                error = None

            return render(request, 'student/register_course.html', {'taken_courses': taken_courses,
                                                                    'taken_credit': st_taken_credit,
                                                                    'courses': ccr,
                                                                    'selected_course': ccr_course,
                                                                    'offered_courses': offered_courses,
                                                                    'warnings': warnings,
                                                                    'error': error,
                                                                    'slots': SLOTS})
        else:
            return redirect('student_home')
    return HttpResponseRedirect('/')


def student_send_approve_view(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student.can_edit_program():
            warnings = []
            errors = []

            st_taken_credit = student.get_taken_credit()
            st_max_credit = student.get_maximum_credit()
            if st_taken_credit == 0:
                errors.append('Empty course list!')

            # Maximum allowed credit rule
            if st_taken_credit > st_max_credit:
                errors.append('You have exceeded the allowed credit limit. You can get a maximum of '
                              + str(st_max_credit) + ' credits')

            context = {'errors': errors, 'warning': warnings}
            return render(request, 'student/send_approve.html', context)
        else:
            return redirect('student_home')
    return HttpResponseRedirect('/')


def student_send_approve(request):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student.can_edit_program():
            student.reg_open_statue = False
            student.approval_statue = False
            student.save()

    return redirect('student_home')


def student_add_taken_course(request, ccr_course_id, act_course_id):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student.can_edit_program():
            success = student.add_taken_course(ccr_course_id, act_course_id)

            if success:
                return redirect('student_register_course')
            else:
                request.session['select_course_error'] = str(success)
        return redirect('student_register_course')
    return HttpResponseRedirect('/')


def student_remove_taken_course(request, ccr_course_id, act_course_id):
    if request.user.is_authenticated and request.user.get_type() is Student:
        student = Student.objects.get(user=request.user)

        if student.can_edit_program():
            try:
                student = Student.objects.get(user=request.user)
                ccr_course = CcrCourse.objects.get(pk=ccr_course_id)
                act_course = Section.objects.get(pk=act_course_id)

                student.remove_taken_course(ccr_course, act_course)

                act_course.quota += 1
                act_course.save()

                return HttpResponseRedirect(reverse('student_register_course'))
            except ObjectDoesNotExist:
                return HttpResponseRedirect(reverse('student_register_course'))
        return redirect('student_register_course')
    return HttpResponseRedirect('/')


def open_courses(request):
    sections = Section.objects.all()

    context = {'open_courses': sections}
    return render(request, 'open_courses.html', context)

@register.filter(name='point')
def point(grade, credit):
    return grade_point(grade) * credit


@register.filter(name='get_info')
def get_info(dictionary, key):
    return dictionary[key]


def generate_password():
    valid_letter = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    valid_digits = '1234567890'
    valid_specs = '+!'

    password = ''
    for i in range(0, 4):
        password += random.choice(valid_letter)
    for i in range(0, 4):
        password += str(random.choice(valid_digits))
    password += random.choice(valid_specs)

    return password


class SendMail(threading.Thread):
    def __init__(self, password, email):
        threading.Thread.__init__(self)
        self.password = password
        self.email = email

    def run(self):
        send_mail(subject='Your application tracking password',
                  message=self.password,
                  from_email=sender,
                  recipient_list=[self.email],
                  fail_silently=False)


# Ali

@login_required
def instructor_advising_students_view(request):
    if request.user.is_authenticated and request.user.get_type() is AcademicStaff:
        students = Student.objects.filter(advisor=request.user.staff.academicstaff)

        context = {
            'students': list(students),
        }
        return render(request, 'academicstaff/students.html', context)
    else:
        return HttpResponseRedirect('/')


class SectionUpdateView(UpdateView):
    model = Section
    template_name = 'academicstaff/change_section.html'
    fields = [
        'quota',
    ]

    def get_success_url(self):
        return reverse("home")


@login_required
def special_quota(request):
    staff = Staff.objects.get(user=request.user)
    user = AcademicStaff.objects.get(staff=staff)
    sections = user.section_set.all()
    context = {
        'sections': sections
    }
    return render(request, 'academicstaff/special_quota.html', context)


@login_required
def open_special_quota(request):
    if request.method == 'POST':
        student_number_id = request.POST.get("student_number")
        section_id = request.POST.get("section")

        section = get_object_or_404(Section, id=section_id)
        student = get_object_or_404(Student, id=student_number_id)

        section.special_quota.add(student)

    return HttpResponseRedirect("/")


@login_required
def harf_notu(request):
    staff = get_object_or_404(Staff, user=request.user)
    user = get_object_or_404(AcademicStaff, staff=staff)
    sections = user.section_set.all()

    context = {
        'sections': sections
    }
    return render(request, 'academicstaff/harf_notu.html', context)


@login_required
def get_section_students(request, pk=None):
    section = get_object_or_404(Section, pk=pk)
    context = {
        'students': section.students.all(),
        'section': section,
    }
    return render(request, 'academicstaff/get_section_students.html', context)


@login_required
def give_note(request):
    if request.method == 'POST':
        grade = request.POST.get("harf_notu")
        st_id = request.POST.get("student_id")
        section_id = request.POST.get("section_id")
        section = get_object_or_404(Section, id=section_id)
        student = get_object_or_404(Student, id=st_id)
        ccr_course = get_object_or_404(CcrCourse, ccr=student.curriculum)

        CompletedCourse.objects.create(
            student=student,
            ccr_course=ccr_course,
            act_course=section.course,
            grade=grade
        )

    return HttpResponseRedirect("/")


@login_required
def studentsOfMyCourses(request):
    # VERDİĞİM DERSLERİN ÖĞRENCİLERİ
    url = 'academicstaff/studentsOfMyCourses.html'
    staff = get_object_or_404(Staff, user=request.user)
    user = get_object_or_404(AcademicStaff, staff=staff)
    sections = Section.objects.all()
    myCourses = []

    for section in sections:
        if user == section.instructor:
            myCourses.append(section)

    takenCourses = TakenCourse.objects.all()
    students = []

    for takenCourse in takenCourses:
        for course in myCourses:
            if takenCourse.act_course == course:
                students.append(takenCourse)

    content = {'students': students}
    return render(request, url, content)

@login_required
def student_courses(request, pk=None):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'taken_courses': student.takencourse_set.all()
    }
    return render(request, 'academicstaff/student_courses.html', context)


@login_required
def instructor_base_view(request):
    url = 'academicstaff/base.html'

    staff = get_object_or_404(Staff, user=request.user)
    user = get_object_or_404(AcademicStaff, staff=staff)
    sections = Section.objects.all()
    myCourses = []

    for section in sections:
        if user == section.instructor:
            myCourses.append(section)

    content = {'myCourses': myCourses}

    return render(request, url, content)


@login_required
def display_transcript(request, st_id=None):
    url = 'academicstaff/display-transcript.html'
    student = get_object_or_404(Student, id=st_id)
    completedCourses = CompletedCourse.objects.filter(student=student)

    return render(request, url, {'completedCourses': completedCourses})


@login_required
def display_schedule(request, st_username):
    if request.user.is_authenticated and request.user.get_type() is AcademicStaff:
        student = User.objects.get(username=st_username).student

        if student:
            schedule = student.get_schedule()
            content = {'dict': schedule, 'slots': SLOTS}
            return render(request, 'student/schedule.html', content)
        else:
            return HttpResponseRedirect('instructor/myStudents')
    else:
        return HttpResponseRedirect('/')


@login_required
def display_curriculum(request, st_username):
    if request.user.is_authenticated and request.user.get_type() is AcademicStaff:
        student = User.objects.get(username=st_username).student

        if student:
            ccr = student.get_curriculum()
            comp_courses = student.get_completed_courses()
            content = {'student': student, 'courses': ccr, 'comp_courses': comp_courses}
            return render(request, 'academicstaff/display-ccr.html', content)
        else:
            return HttpResponseRedirect('instructor/myStudents')
    else:
        return HttpResponseRedirect('/')


@login_required
def openNewSection(request):
    url = 'academicstaff/open-new-section.html'

    if request.method == 'POST':
        form = OpenNewSection(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['course']
            number = form.cleaned_data['number']
            instructor = form.cleaned_data['instructor']
            semester = form.cleaned_data['semester']
        else:
            return redirect('/invalid')
    else:
        form = OpenNewSection()

    return render(request, url, {'form': form})


@login_required
def myCourses(request):
    url = 'academicstaff/my-courses.html'
    staff = get_object_or_404(Staff, user=request.user)
    user = get_object_or_404(AcademicStaff, staff=staff)
    sections = Section.objects.all()
    myCourses = []

    for section in sections:
        if user == section.instructor:
            myCourses.append(section)

    content = {'myCourses': myCourses}
    return render(request, url, content)


@login_required
def myCourseDetails(request, pk=None):
    url = 'academicstaff/my-course-details.html'
    related_section = get_object_or_404(Section, pk=pk)
    students = TakenCourse.objects.filter(act_course=related_section)
    content = {'students': students}
    return render(request, url, content)


@login_required
def grade(request, st_id=None, course_id=None):
    url = 'academicstaff/grade.html'
    student = get_object_or_404(Student, id=st_id)

    if request.method == 'GET':
        form = Grade2Student()
    else:
        form = Grade2Student(request.POST)
        if form.is_valid():
            completedCourse = CompletedCourse(student=student, grade=form.cleaned_data['grade'])
            completedCourse.save(force_insert=True)
            return redirect('/succesfully')

    return render(request, url, {'form': form})


@login_required
def ScheduleApproveOrReject(request, st_id=None):
    url = 'academicstaff/reject.html'
    student = get_object_or_404(Student, id=st_id)
    print(student)

    desiredCourses = TakenCourse.objects.filter(student=student)
    print(desiredCourses)

    for eachCourse in desiredCourses:
        form = ScheduleApproveOrReject(request.GET)
        if form.is_valid():
            form.save()

    return render(request, url, {'form': form})


@login_required
def sectionlar(request):
    url = 'academicstaff/secitons.html'
    sections = Section.objects.all()

    return render(request, url, {'sections': sections})


# Oğuz

# to display academic staff home
def academicStaffs(request):
    return render(request, 'staff/academic-staffs.html', {})


# to display institute staff home
def instituteStaffs(request):
    return render(request, 'staff/institute-staffs.html', {})


# to display grand student home
def grandStudents(request):
    return render(request, 'staff/grand-students.html', {})


# to display institute home
def institute(request):
    return render(request, 'staff/institute.html', {})


# to display institutes
def institutes(request):
    url = 'staff/institutes.html'
    institutes = Institute.objects.all()
    if request.method == 'POST':
        form = AddInstituteForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            head = form.cleaned_data['head']
        else:
            return redirect('/invalid')
    else:
        form = AddInstituteForm()

    return render(request, url, {'institutes': institutes, 'form': form})


# to display details of selected institute
def instituteDetails(request, id=None):
    url = 'staff/institute-details.html'
    instituteDetails = get_object_or_404(Institute, pk=id)
    return render(request, url, {'instituteDetails': instituteDetails})


# to display departments
def departments(request):
    url = 'staff/departments.html'
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            institute = form.cleaned_data['institute']
            head = form.cleaned_data['head']
            return redirect('/departments')
        else:
            return redirect('/invalid')
    else:
        form = AddDepartmentForm()
    departments = Department.objects.order_by('name')
    return render(request, url, {'departments': departments, 'form': form})


# to display details of selected department
def departmentDetails(request, id=None):
    url = 'staff/department-details.html'
    departmentDetails = get_object_or_404(Department, pk=id)
    return render(request, url, {'departmentDetails': departmentDetails})


# to display programs
def programs(request):
    url = 'staff/programs.html'
    if request.method == 'POST':
        form = AddProgramForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            code = form.cleaned_data['code']
            type = form.cleaned_data['type']
            thesis = form.cleaned_data['thesis']
            department = form.cleaned_data['department']
            head = form.cleaned_data['head']
            quota_manager = form.cleaned_data['quota_manager']
            return redirect('/programs')
        else:
            return redirect('/invalid')
    else:
        form = AddProgramForm()
    programs = Program.objects.order_by('name')
    return render(request, url, {'programs': programs, 'form': form})


# to display details of selected program
def programDetails(request, id=None):
    url = 'staff/program-details.html'
    programDetails = get_object_or_404(Program, pk=id)
    return render(request, url, {'programDetails': programDetails})


# to display cirriculums
def cirriculums(request):
    url = 'staff/cirriculums.html'
    if request.method == 'POST':
        form = AddCirriculumForm(request.POST)
        if form.is_valid():
            form.save(request.id)
            program = form.cleaned_data['program']
            year = form.cleaned_data['year']
        else:
            return redirect('/invalid')
    else:
        form = AddCirriculumForm()
    curriculums = Curriculum.objects.all()
    return render(request, url, {'curriculums': curriculums, 'form': form})


# to display details of selected cirriculum
def cirriculumDetails(request, id=None):
    url = 'staff/cirriculum-details.html'
    cirriculumDetails = get_object_or_404(Curriculum, pk=id)
    return render(request, url, {'cirriculumDetails': cirriculumDetails})


# to display all courses and define new course
def courses(request):
    url = 'staff/courses.html'
    if request.method == 'POST':
        addForm = AddCourseForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            code = addForm.cleaned_data['code']
            title = addForm.cleaned_data['title']
            description = addForm.cleaned_data['description']
            credit = addForm.cleaned_data['credit']
            ects_credit = addForm.cleaned_data['ects_credit']
            program = addForm.cleaned_data['program']
            university = addForm.cleaned_data['university']
            # is_valid = addForm.cleaned_data['is_valid']
            # is_deleted = addForm.cleaned_data['is_deleted']
            # created_date = addForm.cleaned_data['created_date']
        else:
            return redirect('/invalid')
    else:
        addForm = AddCourseForm()
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses': courses, 'addForm': addForm})


# to display available courses
def availableCourses(request):
    url = 'staff/available-courses.html'
    availableCourses = Course.objects.filter(is_valid=True)
    return render(request, url, {'availableCourses': availableCourses})


# to display details of selected course
def courseDetails(request, id=None):
    url = 'staff/course-details.html'
    courseDetails = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        editForm = EditCourseForm(request.POST or None, instance=courseDetails)
        if editForm.is_valid():
            editForm.save()
            is_valid = editForm.cleaned_data['is_valid']
        else:
            return redirect('/invalid')
    else:
        editForm = EditCourseForm()

    removeForm = RemoveCourseForm()
    return render(request, url, {'courseDetails': courseDetails, 'editForm': editForm, 'removeForm': removeForm})


# to display courses that would be removed
def removeCourseShow(request):
    url = 'staff/remove-course.html'
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses': courses})


# to display courses that would be closed
def closeCourseShow(request):
    url = 'staff/close-course.html'
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses': courses})


# to display details of selected course and remove
def removeCourse(request, id=None):
    url = 'staff/remove-course-details.html'
    courseDetails = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        removeForm = RemoveCourseForm(request.POST or None, instance=courseDetails)
        if removeForm.is_valid():
            removeForm.save()
            is_deleted = removeForm.cleaned_data['is_deleted']
        else:
            return redirect('/invalid')
    else:
        removeForm = RemoveCourseForm()
    return render(request, url, {'courseDetails': courseDetails, 'removeForm': removeForm})


# to dispaly details of selected course and close
def closeCourse(request, id=None):
    url = 'staff/close-course-details.html'
    courseDetails = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        editForm = EditCourseForm(request.POST or None, instance=courseDetails)
        if editForm.is_valid():
            editForm.save()
            is_valid = editForm.cleaned_data['is_valid']
        else:
            return redirect('/invalid')
    else:
        editForm = EditCourseForm()
    return render(request, url, {'courseDetails': courseDetails, 'editForm': editForm})


# to display course types
def courseTypes(request):
    url = 'staff/course-types.html'
    if request.method == 'POST':
        form = AddCourseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            code = form.cleaned_data['code']
        else:
            return redirect('/invalid')
    else:
        form = AddCourseTypeForm()
    courseTypes = CourseType.objects.all()
    return render(request, url, {'courseTypes': courseTypes, 'form': form})


# to display sections
def sections(request):
    url = 'staff/sections.html'
    if request.method == 'POST':
        form = AddSectionForm(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['course']
            number = form.cleaned_data['number']
            instructor = form.cleaned_data['instructor']
            semester = form.cleaned_data['semester']
        else:
            return redirect('/invalid')
    else:
        form = AddSectionForm()
    sections = Section.objects.order_by('-year')
    return render(request, url, {'sections': sections, 'form': form})


# to display details of selected section
def sectionDetails(request, id=None):
    url = 'staff/section-details.html'
    sectionDetails = get_object_or_404(Section, pk=id)
    return render(request, url, {'sectionDetails': sectionDetails})


# to make registration of academic staff - i
def academicStaffRegistrationI(request):
    url = 'staff/academic-staff-registration-i.html'
    if request.method == 'POST':
        formU = AddUserForm(request.POST)
        if formU.is_valid():
            formU.save()
            print(formU)
            return redirect('/academic-staff-registration-ii')
        else:
            return redirect('/invalid')
    else:
        formU = AddUserForm()
    return render(request, url, {'formU': formU})


# to make registration of academic staff - ii
def academicStaffRegistrationII(request):
    url = 'staff/academic-staff-registration-ii.html'
    desiredUser = User.objects.all().last()
    if request.method == 'POST':
        formS = AddStaffForm(request.POST)
        if formS.is_valid():
            staff = Staff(user=desiredUser, tc=formS.cleaned_data['tc'], gender=formS.cleaned_data['gender'],
                          main_email=formS.cleaned_data['main_email'], school_email=formS.cleaned_data['school_email'],
                          address=formS.cleaned_data['address'], birthday=formS.cleaned_data['birthday'],
                          city=formS.cleaned_data['birthday'])
            staff.save(force_insert=True)

            return redirect('/succesfully')
        else:
            return redirect('/invalid')
    else:
        formS = AddStaffForm()
    return render(request, url, {'formS': formS})


# to display all academic staffs
def allAcademicStaff(request):
    url = 'staff/all-academic-staff.html'
    if request.method == 'POST':
        formA = AddAcademicStaffForm(request.POST)
        if formA.is_valid():
            formA.save()
        else:
            return redirect('/invalid')
    else:
        formA = AddAcademicStaffForm()
    academicStaffs = AcademicStaff.objects.order_by('staff')
    content = {'academicStaffs': academicStaffs, 'formA': formA}
    return render(request, url, content)


# to display details of selected academic staff
def academicStaffDetails(request, id=None):
    url = 'staff/academic-staff-details.html'
    academicStaffDetails = get_object_or_404(AcademicStaff, pk=id)
    return render(request, url, {'academicStaffDetails': academicStaffDetails})


# to display institute heads
def instituteHeads(request):
    content = Institute.objects.order_by('head')
    instituteHeads = {'instituteHeads': content}
    return render(request, 'staff/institute-heads.html', instituteHeads)


# to display department heads
def departmentHeads(request):
    content = Department.objects.order_by('dept_head')
    departmentHeads = {'departmentHeads': content}
    return render(request, 'staff/department-heads.html', departmentHeads)


# to display program heads
def programHeads(request):
    content = Program.objects.order_by('head')
    programHeads = {'programHeads': content}
    return render(request, 'staff/program-heads.html', programHeads)


# to display quoata managers and add new
# def quoataManagers(request):
#    url = 'quoata-managers.html'
#    if request.method == 'POST':
#        form = AddQuoataManagerForm(request.POST)
#        if form.is_valid():
#            form.save()
#        else:
#            return redirect('/invalid')
#    else:
#        form = AddQuoataManagerForm()
#    quoataManagers = Program.objects.order_by('quota_manager')
#    return render(request, url, {'quoataManagers': quoataManagers, 'form': form})


# to display all institute staff
def allInstituteStaff(request):
    url = 'staff/all-institute-staff.html'
    instituteStaffs = Staff.objects.order_by('tc')
    content = {'instituteStaffs': instituteStaffs}
    return render(request, url, content)


# to display all grand student
def allGrandStudent(request):
    content = Student.objects.order_by('user')
    grandStudents = {'grandStudents': content}
    return render(request, 'staff/all-grand-student.html', grandStudents)


# to display details of selected grand student
def grandStudentDetails(request, id=None):
    url = 'staff/grand-student-details.html'
    grandStudentDetails = get_object_or_404(Student, pk=id)
    return render(request, url, {'grandStudentDetails': grandStudentDetails})


# to make registration of visitor - i
def applicationI(request):
    url = 'staff/student-application-i.html'
    if request.method == 'POST':
        formU = AddUserForm(request.POST)
        if formU.is_valid():
            formU.save()
            print(formU)
            return redirect('/application-ii')
        else:
            return redirect('/invalid')
    else:
        formU = AddUserForm()
    return render(request, url, {'formU': formU})


# to make registration of staff - i
def instituteStaffI(request):
    url = 'staff/all-institute-staff.html'
    if request.method == 'POST':
        formU = AddUserForm(request.POST)
        if formU.is_valid():
            formU.save()
        else:
            return redirect('#')
    else:
        formU = AddUserForm()
    return render(request, url, {'formU': formU})


# to make registration of visitor - ii
def applicationII(request):
    url = 'staff/student-application-ii.html'
    desiredUser = User.objects.all().last()
    if request.method == 'POST':
        formV = AddVisitorForm(request.POST)
        if formV.is_valid():
            visitor = Visitor(user=desiredUser, tc=formV.cleaned_data['tc'], birthday=formV.cleaned_data['birthday'],
                              gender=formV.cleaned_data['gender'],
                              address=formV.cleaned_data['address'], city=formV.cleaned_data['city'],
                              degree=formV.cleaned_data['degree'],
                              university=formV.cleaned_data['university'], gpa=formV.cleaned_data['gpa'],
                              ales=formV.cleaned_data['ales'],
                              yds=formV.cleaned_data['yds'], program=formV.cleaned_data['program'])
            visitor.save(force_insert=True)
            return redirect('/succesfully')
        else:
            return redirect('/invalid')
    else:
        formV = AddVisitorForm()
    return render(request, url, {'formV': formV})


# to make registration of staff - ii


# to apply
def apply(request):
    url = "staff/apply.html"
    if request.method == 'POST':
        form = AddVisitorForm(request.POST)
        user_form = AddUserForm(request.POST)

        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
        else:
            return redirect('/invalid')
    else:
        form = AddVisitorForm()
        user_form = AddUserForm()
    return render(request, url, {'form': form, 'user_form': user_form})


# to display all applies
def applies(request):
    content = Visitor.objects.order_by('user')
    applies = {'applies': content}
    return render(request, 'staff/applies.html', applies)


# to display details of selected application
def applicationDetails(request, tc=None):
    url = 'staff/application-details.html'
    visitorDetails = get_object_or_404(Visitor, tc=tc)
    desiredUser = visitorDetails.user
    if request.method == 'GET':
        form = AddStudentForm()
    else:
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = Student(user=desiredUser, st_id=form.cleaned_data['st_id'],
                              st_email=form.cleaned_data['st_email'], curriculum=form.cleaned_data['curriculum'],
                              program=form.cleaned_data['program'], advisor=form.cleaned_data['advisor'],
                              hold_state=form.cleaned_data['hold_state'],
                              reg_open_statue=form.cleaned_data['reg_open_statue'],
                              approval_statue=form.cleaned_data['approval_statue'])
            student.save(force_insert=True)
            return redirect('/succesfully')
    applicationDetails = {'visitorDetails': visitorDetails, 'form': form}
    return render(request, url, applicationDetails)


# to remove selected application
def removeSelectedApplication(request, tc=None):
    url = 'staff/applies.html'
    visitor = Visitor.objects.get(tc=tc)
    visitor.delete()
    return render(request, url, {'action': 'Delete tasks'})


# to remove all applications
def removeAllAplications(request):
    url = 'staff/succesfully.html'
    all_visitors = Visitor.objects.all()
    all_visitors.delete()
    return render(request, url, {'action': 'Delete tasks'})


# to remove all sections
def removeAllSections(request):
    url = 'staff/succesfully.html'
    all_sections = Section.objects.all()
    all_sections.delete()
    return render(request, url, {'action': 'Delete tasks'})


# to redirect succesfully
def succesfully(request):
    url = 'staff/succesfully.html'
    return render(request, url, {})


# to redirect invalid
def invalid(request):
    url = 'staff/invalid.html'
    return render(request, url, {})


# to display all completed courses for all students in the system
def allCompletedCourses(request):
    url = 'staff/allCompletedCourses.html'
    programs = Program.objects.order_by('name')
    return render(request, url, {'programs': programs})


# to display details of selected department-course relationship
def allCompletedCoursesDetails(request, id=None):
    url = 'staff/all-completed-courses-details.html'
    relatedProgram = get_object_or_404(Program, pk=id)
    courses = Course.objects.filter(program__name=relatedProgram.name)
    return render(request, url, {'courses': courses})


# to display details of selected course from all completed course
def selectedCompletedCourseDetails(request, id=None):
    # to determine the redirecting page
    url = 'staff/selected-completed-course-details.html'

    # to retrieve data of clicked course
    courseDetails = get_object_or_404(Course, pk=id)

    # to retrieve data of all completed courses
    completedCourses = CompletedCourse.objects.all()

    # to store students of relevant completed course
    student = []

    grade = []

    # to find related courses in the completed courses list
    for i in completedCourses:

        # to make matching desired course with all course
        if courseDetails.title == i.act_course.title:
            grade = i.grade
            student = i.student.st_id

    return render(request, url, {'grade': grade, 'student': student})