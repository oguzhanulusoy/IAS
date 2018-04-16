"""CSE490 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Institute import views as v
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', v.base),
    path('academic-staffs/', v.academicStaffs),
    path('institute-staffs/', v.instituteStaffs),
    path('institute/', v.institute),
    path('grand-students/', v.grandStudents),
    path('institutes/', v.institutes),
    path('departments/', v.departments),
    path('programs/', v.programs),
    path('program-details/<pk>', v.programDetails),
    path('cirriculums/', v.cirriculums),
    path('courses/', v.courses),
    path('course-types/', v.courseTypes),
    path('sections/', v.sections),
    path('all-academic-staff/', v.allAcademicStaff),
    path('institute-heads/', v.instituteHeads),
    path('department-heads/', v.departmentHeads),
    path('program-heads/', v.programHeads),
    path('quoata-managers/', v.quoataManagers),
    path('all-institute-staff/', v.allInstituteStaff),
    path('all-grand-student/', v.allGrandStudent),
    path('applies/', v.applies),

] + static(settings.STATIC_URL.lstrip('/'), document_root=settings.STATIC_ROOT)

