from django.shortcuts import render
from .models import *

def displayStudents(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


def base(request):
    return render(request, 'base.html', {})