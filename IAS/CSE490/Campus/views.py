from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *

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
    content = Department.objects.order_by('name')
    departments = {'departments' : content}
    return render(request, 'departments.html', departments)

def programs(request):
    content = Program.objects.order_by('name')
    programs = {'programs' : content}
    return render(request, 'programs.html', programs)

def programDetails(request, pk=None):
    post = get_object_or_404(Program, pk=pk)
    programDetails = {'post': post}
    print(programDetails)
    return render(request, 'program-details.html', programDetails)

def cirriculums(request):
    content = Curriculum.objects.all()
    curriculums = {'curriculums' : content}
    return render(request, 'cirriculums.html', curriculums)

def courses(request):
    content = Course.objects.order_by('-created_date')
    courses = {'courses' : content}
    return render(request, 'courses.html', courses)

def courseTypes(request):
    content = CourseType.objects.all()
    courseTypes = {'courseTypes' : content}
    return render(request, 'course-types.html', courseTypes)

def sections(request):
    content = Section.objects.order_by('-year')
    sections = {'sections' : content}
    return render(request, 'sections.html', sections)
