from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import *

def base(request):
    return render(request, 'base.html', {})

def academicStaffs(request):
    return render(request, 'academic-staffs.html', {})

def instituteStaffs(request):
    return render(request, 'institute-staffs.html', {})

def grandStudents(request):
    return render(request, 'grand-students.html', {})

def institute(request):
    return render(request, 'institute.html', {})

def institutes(request):
    content = Institute.objects.order_by('-establishedDate')
    institutes = {'institutes' : content}
    return render(request, 'institutes.html', institutes)

def departments(request):
    url = 'departments.html'
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
    return render(request, url, {'departments' : departments, 'form': form})

def programs(request):
    url = 'programs.html'
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
    return render(request, url, {'programs' : programs, 'form' : form})

def programDetails(request, id=None):
    url = 'program-details.html'
    programDetails = get_object_or_404(Program, pk=id)
    return render(request, url, {'programDetails' : programDetails})

def cirriculums(request):
    url = 'cirriculums.html'
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
    return render(request, url, {'curriculums' : curriculums, 'form' : form})

 



##############################################





def courses(request):
    url = 'courses.html'
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
            is_valid = addForm.cleaned_data['is_valid']
            is_deleted = addForm.cleaned_data['is_deleted']
            created_date = addForm.cleaned_data['created_date']
        else:
            return redirect('/invalid')
    else:
        addForm = AddCourseForm()
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses' : courses, 'addForm' : addForm})



def courseDetails(request, id=None):
    url = 'course-details.html'
    courseDetails = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        editForm = EditCourseForm(request.POST or None, instance=courseDetails)
        if editForm.is_valid() :
            editForm.save()
            is_valid = editForm.cleaned_data['is_valid']
        else:
            return redirect('/invalid')
    else:
        editForm = EditCourseForm()

    removeForm = RemoveCourseForm()
    return render(request, url, {'courseDetails' : courseDetails, 'editForm' : editForm, 'removeForm' : removeForm} )


def removeCourseShow(request):
    url = 'remove-course.html'
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses' : courses})


def closeCourseShow(request):
    url = 'close-course.html'
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses' : courses})




def removeCourse(request, id=None):
    url = 'remove-course-details.html'
    courseDetails = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        removeForm = RemoveCourseForm(request.POST or None, instance=courseDetails)
        if removeForm.is_valid() :
            removeForm.save()
            is_deleted = removeForm.cleaned_data['is_deleted']
        else:
            return redirect('/invalid')
    else:
        removeForm = RemoveCourseForm()
    return render(request, url, {'courseDetails' : courseDetails, 'removeForm' : removeForm} )



def closeCourse(request, id=None):
    url = 'close-course-details.html'
    courseDetails = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        editForm = EditCourseForm(request.POST or None, instance=courseDetails)
        if editForm.is_valid() :
            editForm.save()
            is_valid = editForm.cleaned_data['is_valid']
        else:
            return redirect('/invalid')
    else:
        editForm = EditCourseForm()
    return render(request, url, {'courseDetails' : courseDetails, 'editForm' : editForm} )













def courseTypes(request):
    url = 'course-types.html'
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
    return render(request, url, {'courseTypes' : courseTypes, 'form' : form})

def sections(request):
    url = 'sections.html'
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
    return render(request, url, {'sections' : sections, 'form' : form})

def academicStaffRegistrationI(request):
    url = 'academic-staff-registration-i.html'
    if request.method == 'POST':
        formU = AddUserForm(request.POST)
        if formU.is_valid():
            formU.save()
            return redirect('/academic-staff-registration-ii')
        else:
            return redirect('/invalid')
    else:
        formU = AddUserForm()
    return render(request, url, {'formU' : formU})

def academicStaffRegistrationII(request):
    url = 'academic-staff-registration-ii.html'
    if request.method == 'POST':
        formS = AddStaffForm(request.POST)
        if formS.is_valid():
            formS.save()
            return redirect('/succesfully')
        else:
            return redirect('/invalid')
    else:
        formS = AddStaffForm()
    return render(request, url, {'formS' : formS})

def succesfully(request):
    url = 'succesfully.html'
    return render(request, url, {})

'''Döneceğim buraya '''
def allAcademicStaff(request):
    url = 'all-academic-staff.html'
    if request.method == 'POST':
        formA = AddAcademicStaffForm(request.POST)
        if formA.is_valid():
            formA.save()
        else:
            return redirect('/invalid')
    else:
        formA = AddAcademicStaffForm()
    academicStaffs = AcademicStaff.objects.order_by('staff')
    content = {'academicStaffs' : academicStaffs, 'formA' : formA}
    return render(request, url, content)

def instituteHeads(request):
    content = Institute.objects.order_by('head')
    instituteHeads = {'instituteHeads' : content}
    return render(request, 'institute-heads.html', instituteHeads)

def departmentHeads(request):
    content = Department.objects.order_by('head')
    departmentHeads = {'departmentHeads' : content}
    return render(request, 'department-heads.html', departmentHeads)

def programHeads(request):
    content = Program.objects.order_by('head')
    programHeads = {'programHeads' : content}
    return render(request, 'program-heads.html', programHeads)

def quoataManagers(request):
    url = 'quoata-managers.html'
    if request.method == 'POST':
        form = AddQuoataManagerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('/invalid')
    else:
        form = AddQuoataManagerForm()
    quoataManagers = Program.objects.order_by('quota_manager')
    return render(request, url, {'quoataManagers' : quoataManagers, 'form' : form})

def allInstituteStaff(request):
    url = 'all-institute-staff.html'
    if request.method == 'POST':
        formU = AddUserForm(request.POST)
        formS = AddStaffForm(request.POST)

    content = Staff.objects.order_by('tc')
    instituteStaffs = {'instituteStaffs' : content}
    return render(request, url, instituteStaffs)

def allGrandStudent(request):
    content = Student.objects.order_by('user')
    grandStudents = {'grandStudents' : content}
    return render(request, 'all-grand-student.html', grandStudents)

def applicationI(request):
    url = 'student-application-i.html'
    if request.method == 'POST':
        formU = AddUserForm(request.POST)
        if formU.is_valid():
            formU.save()
            return redirect('/application-ii')
        else:
            return redirect('/invalid')
    else:
        formU = AddUserForm()
    return render(request, url, {'formU' : formU})

def applicationII(request):
    url = 'student-application-ii.html'
    if request.method == 'POST':
        formV = AddVisitorForm(request.POST)
        if formV.is_valid():
            formV.save()
            return redirect('/succesfully')
        else:
            return redirect('/invalid')
    else:
        formV = AddVisitorForm()
    return render(request, url, {'formV' : formV})

def applies(request):
    content = Visitor.objects.order_by('user')
    applies = {'applies' : content}
    return render(request, 'applies.html', applies)







##############################################


def applicationDetails(request, id=None):
    url = 'application-details.html'
    userDetails = get_object_or_404(User, pk=id)
    visitorDetails = get_object_or_404(Visitor, pk=userDetails.id)
    if request.method == 'POST':
        form = AddStudentForm(request.POST or None, instance=userDetails)
        if form.is_valid():
            form.save()
            userDetails = form.cleaned_data['user']
            st_id = form.cleaned_data['st_id']
            st_email = form.cleaned_data['st_email']
            curriculum = form.cleaned_data['curriculum']
            program = form.cleaned_data['program']
            advisor = form.cleaned_data['advisor']
            hold_state = form.cleaned_data['hold_state']
            reg_open_statue = form.cleaned_data['reg_open_statue']
            approval_statue = form.cleaned_data['approval_statue']
        else:
            return redirect('/invalid')
    else:
        form = AddStudentForm()
    applicationDetails = {'visitorDetails' : visitorDetails, 'userDetails' : userDetails, 'form' : form}
    return render(request, url, applicationDetails)








##############################################





def invalid(request):
    url = 'invalid.html'
    return render(request, url, {})