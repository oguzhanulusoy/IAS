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


    # Ali
    path('instructor/', instructor_base_view, name='instructor_base_view'),
    path('instructor/curriculum/<st_username>/', display_curriculum),
    path('instructor/transcript/<st_username>/', display_transcript),
    path('instructor/schedule/<st_username>/', display_schedule),
    path('instructor/students', instructor_advising_students_view, name="advising_students_view"),

    path('student_courses/<pk>/', student_courses, name="student_courses"),
    path('special_quota', special_quota, name='special_quota'),
    path('open_special_quota', open_special_quota, name='open_special_quota'),
    path('harf_notu/', harf_notu, name='harf_notu'),
    path('get_section_students/<pk>/', get_section_students, name="get_section_students"),
    path('give_note/', give_note, name="give_note"),
    path('changeQuota/<pk>/', SectionUpdateView.as_view()),
    path('studentsOfMyCourses/', studentsOfMyCourses, name="studentsOfMyCourses"),


    path('myCourses/', myCourses, name="myCourses"),
    path('myCourseDetails/<pk>/', myCourseDetails),
    path('grade/<st_id>/', grade),
    path('openNewSection/', openNewSection),
    path('Reject/<st_id>/', ScheduleApproveOrReject, name="ScheduleApproveOrReject"),
    path('sectionlar/', sectionlar, name="sectionlar"),

    # Oğuz

    path('base/', instructor_base_view),
    path('academic-staffs/', academicStaffs),
    path('institute-staffs/', instituteStaffs),
    path('institute/', institute),
    path('grand-students/', grandStudents),
    path('institutes/', institutes),
    path('departments/', departments),
    path('programs/', programs),
    path('program-details/<id>/', programDetails),
    path('cirriculums/', cirriculums),
    path('courses/', courses),
    path('course-types/', courseTypes),
    path('sections/', sections),
    path('all-academic-staff/', allAcademicStaff),
    path('institute-heads/', instituteHeads),
    path('department-heads/', departmentHeads),
    path('program-heads/', programHeads),
    # path('quoata-managers/', quoataManagers),
    path('all-institute-staff/', allInstituteStaff),
    path('all-grand-student/', allGrandStudent),
    path('applications/', applies),
    path('invalid/', invalid),
    path('academic-staff-registration-i/', academicStaffRegistrationI),
    path('academic-staff-registration-ii/', academicStaffRegistrationII),
    path('succesfully/', succesfully),
    path('application-i/', applicationI),
    path('application-ii/', applicationII),
    path('application-details/<tc>/', applicationDetails),
    path('course-details/<id>/', courseDetails),
    path('remove-course/', removeCourseShow),
    path('remove-course-details/<id>/', removeCourse),
    path('close-course/', closeCourseShow),
    path('close-course-details/<id>/', closeCourse),
    path('institute-details/<id>/', instituteDetails),
    path('department-details/<id>/', departmentDetails),
    path('cirriculum-details/<id>/', cirriculumDetails),
    path('section-details/<id>/', sectionDetails),
    path('academic-staff-details/<id>/', academicStaffDetails),
    path('grand-student-details/<id>/', grandStudentDetails),
    path('available-courses/', availableCourses),
    path('all-completed-courses/', allCompletedCourses),
    path('all-completed-courses-details/<id>/', allCompletedCoursesDetails),
    path('selected-completed-course-details/<id>/', selectedCompletedCourseDetails),
    path('removeSelectedApplication/<tc>/', removeSelectedApplication),
    path('removeAllAplications/', removeAllAplications),
    path('removeAllSections/', removeAllSections),
    path('apply/', apply),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL.lstrip('/'), document_root=settings.STATIC_ROOT)