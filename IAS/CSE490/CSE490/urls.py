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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('/', v.home),
    path('admin/', admin.site.urls),
    path('base/', v.base),
    path('academic-staffs/', v.academicStaffs),
    path('institute-staffs/', v.instituteStaffs),
    path('institute/', v.institute),
    path('grand-students/', v.grandStudents),
    path('institutes/', v.institutes),
    path('departments/', v.departments),
    path('programs/', v.programs),
    path('program-details/<id>/', v.programDetails),
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
    path('applications/', v.applies),
    path('invalid/', v.invalid),
    path('academic-staff-registration-i/', v.academicStaffRegistrationI),
    path('academic-staff-registration-ii/', v.academicStaffRegistrationII),
    path('succesfully/', v.succesfully),
    path('application-i/', v.applicationI),
    path('application-ii/', v.applicationII),
    path('application-details/<tc>/', v.applicationDetails),
    path('course-details/<id>/', v.courseDetails),
    path('remove-course/', v.removeCourseShow),
    path('remove-course-details/<id>/', v.removeCourse),
    path('close-course/', v.closeCourseShow),
    path('close-course-details/<id>/', v.closeCourse),
    path('institute-details/<id>/', v.instituteDetails),
    path('department-details/<id>/', v.departmentDetails),
    path('cirriculum-details/<id>/', v.cirriculumDetails),
    path('section-details/<id>/', v.sectionDetails),
    path('academic-staff-details/<id>/', v.academicStaffDetails),
    path('grand-student-details/<id>/', v.grandStudentDetails),
    path('available-courses/', v.availableCourses),
    path('all-completed-courses/', v.allCompletedCourses),
    path('all-completed-courses-details/<id>/', v.allCompletedCoursesDetails),
    path('selected-completed-course-details/<id>/', v.selectedCompletedCourseDetails),
    path('removeSelectedApplication/<tc>/', v.removeSelectedApplication),
    path('removeAllAplications/', v.removeAllAplications),
    path('removeAllSections/', v.removeAllSections),
    path('apply/',v.apply),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('makeAnnouncement/', v.makeAnnouncement),
    path('defineExamDate/', v.defineExamDate),



] + static(settings.STATIC_URL.lstrip('/'), document_root=settings.STATIC_ROOT)

