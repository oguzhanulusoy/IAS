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

def programDetails(request, pk=None):
    post = get_object_or_404(Program, pk=pk)
    programDetails = {'post': post}
    print(programDetails)
    return render(request, 'program-details.html', programDetails)

def cirriculums(request):
    url = 'cirriculums.html'
    if request.method == 'POST':
        form = AddCirriculumForm(request.POST)
        if form.is_valid():
            form.save()
            program = form.cleaned_data['program']
            year = form.cleaned_data['year']
        else:
            return redirect('/invalid')
    else:
        form = AddCirriculumForm()
    curriculums = Curriculum.objects.all()
    return render(request, url, {'curriculums' : curriculums, 'form' : form})

def courses(request):
    url = 'courses.html'
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('/invalid')
    else:
        form = AddCourseForm()
    courses = Course.objects.order_by('-created_date')
    return render(request, url, {'courses' : courses, 'form' : form})

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

def allAcademicStaff(request):
    url = 'all-academic-staff.html'
    if request.method == 'POST':
        formA = AddAcademicStaffForm(request.POST)
        formS = AddStaffForm(request.POST)
        formU = AddUserForm(request.POST)
        if formA.is_valid() and formS.is_valid() and formU.is_valid():
            formA.save()
            formS.save()
            formU.save()
        else:
            return redirect('/invalid')
    else:
        formA = AddAcademicStaffForm()
        formS = AddStaffForm()
        formU = AddUserForm()
    academicStaffs = AcademicStaff.objects.order_by('staff')
    content = {'academicStaffs' : academicStaffs, 'formU' : formU, 'formS' : formS, 'formA' : formA}
    return render(request, url, content)

def instituteHeads(request):
    content = Institute.objects.order_by('head')
    instituteHeads = {'instituteHeads' : content}
    return render(request, 'institute-heads.html', instituteHeads)

def departmentHeads(request):
    content = Department.objects.order_by('dept_head')
    departmentHeads = {'departmentHeads' : content}
    return render(request, 'department-heads.html', departmentHeads)

def programHeads(request):
    content = Program.objects.order_by('head')
    programHeads = {'programHeads' : content}
    return render(request, 'program-heads.html', programHeads)

def quoataManagers(request):
    content = Program.objects.order_by('quota_manager')
    quoataManagers = {'quoataManagers' : content}
    return render(request, 'quoata-managers.html', quoataManagers)

def allInstituteStaff(request):
    content = Staff.objects.order_by('tc')
    instituteStaffs = {'instituteStaffs' : content}
    return render(request, 'all-institute-staff.html', instituteStaffs)

def allGrandStudent(request):
    content = Student.objects.order_by('user')
    grandStudents = {'grandStudents' : content}
    return render(request, 'all-grand-student.html', grandStudents)

def applies(request):
    content = Visitor.objects.order_by('user')
    applies = {'applies' : content}
    return render(request, 'applies.html', applies)

def invalid(request):
    url = 'invalid.html'
    return render(request, url, {})