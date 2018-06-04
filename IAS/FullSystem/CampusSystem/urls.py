"""CampusSystem URL Configuration

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

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from baseapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    url(r'^$', index, name='home'),

    # Login
    url('login/$', login_view, name='login'),

    # Logout
    url('logout/$', logout_view, name='logout'),

    # User
    url('profile/$', profile_view, name='profile'),
    url('information', personal_information_view, name='personal_information'),


    # Student
    url('student/$', student_home_view, name='student_home'),
    url('student/ccr/$', student_ccr_view, name='student_ccr'),
    url('student/ccr/external/$', student_ccr_external_view, name='student_ccr_external'),
    url('student/schedule/$', student_schedule_view, name='student_schedule'),
    url('student/transcript/$', student_transcript_view, name='student_transcript'),
    url('student/register/$', student_register_course_view, name='student_register_course'),
    url('student/register/(\d+)/$', student_register_course_view, name='student_register_course_param'),
    url('student/register/approval/$', student_send_approve_view, name='student_send_approve'),
    url('student/register/approval/send/$', student_send_approve, name='student_send_approve_last'),

    url('student/add/(\d+)/(\d+)/$', student_add_taken_course, name='student_add_taken_course'),
    url('student/remove/(\d+)/(\d+)/$', student_remove_taken_course, name='student_remove_taken_course'),

    # Course
    url('open_courses', open_courses, name='open_courses'),

    # Application Pages
    url('application/$', application, name='application'),


    

    # Oğuz

#### YENi EKLENENLER ####
    #### MAIN MENUS ####
    path('staff/', staff_home_view),

    path('academic-staff/', academicStaff, name="academic-staff"),
    path('institute-staff/', instituteStaff, name="institute-staff"),
    path('grad-student/', gradStudent),
    path('institute/', institute, name="institute"),

    #### SUB MENU OF INSTITUTE ####
    path('institutes/', institutes, name="institutes"),
    path('departments/', departments, name="departments"),
    path('programs/', programs, name="programs"),
    path('curriculums/', curriculums, name="curriculums"),
    path('courses/', courses, name="courses"),
    path('available-courses/', availableCourses, name="available-courses"),
    path('remove-course/', removeCourseHome, name="remove-course"),
    path('open-or-close-course/', openCloseCourseHome, name="open-or-close-course"),
    path('course-types/', courseTypes, name="course-types"),
    path('sections/', sections, name="sections"),
    path('define-exam-dates/', defineExamDates, name="define-exam-dates"),
    path('make-announcement/', makeAnnouncements, name="make-announcement"),

    path('institute-details/<id>/', instituteDetails, name="institute-details"),
    path('department-details/<id>/', departmentDetails, name="department-details"),
    path('program-details/<id>/', programDetails, name="program-details"),
    path('curriculum-details/<id>/', curriculumDetails, name="curriculum-details"),
    path('course-details/<id>/', courseDetails, name="course-details"),
    path('remove-course-details/<id>/', removeCourse, name="remove-course-details"),
    path('open-or-close-course-details/<id>/', openCloseCourse, name="open-or-close-course-details"),
    path('section-details/<id>/', sectionDetails, name="section-details"),
    path('exam-details/<id>/', examDetails, name="exam-details"),
    path('announcement-details/<id>/', announcementDetails, name="announcement-details"),


    #### SUB MENU OF ACADEMIC STAFF ####
    path('all-academic-staff/', allAcademicStaff, name="all-academic-staff"),
    path('add-academic-staff-i/', addAcademicStaffI, name="add-academic-staff-i"),
    path('add-academic-staff-ii/', addAcademicStaffII, name="add-academic-staff-ii"),
    path('institute-heads/', instituteHeads, name="institute-heads"),
    path('department-heads/', departmentHeads, name="department-heads"),
    path('program-heads/', programHeads, name="program-heads"),

    path('academic-staff-details/<id>/', academicStaffDetails, name="academic-staff-details"),
    
    

    #### SUB MENU OF INSTITUTE STAFF ####

    path('all-institute-staff/', allInstituteStaff, name="all-institute-staff"),
    path('institute-staff-details/<tc>/', instituteStaffDetails, name="institute-staff-details"),
    

    #### SUB MENU OF GRAD STUDENTS ####

    path('all-grad-student/', allGradStudent, name="all-grad-student"),
    path('applications/', applications, name="applications"),
    path('application-details/<tc>/', applicationDetails, name="application-details"),


    path('display-students/', displayStudent),
    path('display-student-details/<st_id>/', displayStudentDetails),

##### ALİ


    path('instructor/', instructor_home_view, name='instructor_home_view'),
    path('students-in-my-courses/', studentsInMyCourses),

    path('my-students/', myStudents),
    path('my-courses/', myCourses),
    path('my-course-details/<pk>/', myCourseDetails),
    path('grade/<st_id>/', grade),
    path('all-sections/', sectionlar),
    path('change-quota/<pk>/', SectionUpdateView.as_view()),
    path('special-quota/', special_quota),
    path('open-special-quota/', open_special_quota, name="open-special-quota"),
    path('display-transcript/<st_id>/', display_transcript),
    path('display-schedule/<st_id>/', displaySchedule),
    path('display-ccr/<st_id>/', displayCCR),
    path('display-curriculum/<st_id>/', displayCurriculum),
    






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL.lstrip('/'), document_root=settings.STATIC_ROOT)