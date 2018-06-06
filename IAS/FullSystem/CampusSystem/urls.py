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


    

#### YENi EKLENENLER - OGUZ ####
    path('staff/', staff_home_view),
    path('academic-staff/', academicStaff, name="academic-staff"),
    path('institute-staff/', instituteStaff, name="institute-staff"),
    path('grad-students/', gradStudents, name="grad-students"),
    path('institute/', institute, name="institute"),
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
    path('all-academic-staff/', allAcademicStaff, name="all-academic-staff"),
    path('add-academic-staff-i/', addAcademicStaffI, name="add-academic-staff-i"),
    path('add-academic-staff-ii/', addAcademicStaffII, name="add-academic-staff-ii"),
    path('institute-heads/', instituteHeads, name="institute-heads"),
    path('department-heads/', departmentHeads, name="department-heads"),
    path('program-heads/', programHeads, name="program-heads"),
    path('academic-staff-details/<id>/', academicStaffDetails, name="academic-staff-details"),
    path('all-institute-staff/', allInstituteStaff, name="all-institute-staff"),
    path('institute-staff-details/<tc>/', instituteStaffDetails, name="institute-staff-details"),
    path('all-grad-students/', allGradStudents, name="all-grad-students"),
    path('applications/', applications, name="applications"),
    path('application-details/<tc>/', applicationDetails, name="application-details"),
    path('display-students/', displayStudent, name="display-students"),
    path('display-student-details/<st_id>/', displayStudentDetails, name="display-student-details"),
    path('all-completed-courses/', allCompletedCourses, name="all-completed-courses"),
    path('all-completed-courses-details/<id>/', allCompletedCoursesDetails, name="all-completed-courses-details"),
    path('selected-completed-course-details/<id>/', selectedCompletedCourseDetails, name="selected-completed-course-details"),
    path('succesfully/', succesfully, name="succesfully"),
    path('invalid/', invalid, name="invalid"),
    path('grad-student-details/<st_id>/', gradStudentDetails, name="grad-student-details"),
    url(r'^delete-selected-application/(?P<tc>\d+)/$', deleteSelectedApplication, name='delete-selected-application'),
    url(r'^reject-selected-application/(?P<tc>\d+)/$', rejectSelectedApplication, name='reject-selected-application'),
    url(r'^delete-all-applications/$', deleteAllApplications, name='delete-all-applications'),
    url(r'^delete-selected-exam-date/(?P<id>\d+)/$', deleteSelectedExamDate, name='delete-selected-exam-date'),
    url(r'^delete-all-exams/$', deleteAllExams, name='delete-all-exams'),
    url(r'^delete-all-announcements/$', deleteAllAnnouncements, name='delete-all-announcements'),
    url(r'^delete-all-sections/$', deleteAllSections, name='delete-all-sections'),
    url(r'^delete-selected-section/(?P<id>\d+)/$', deleteSelectedSection, name='delete-selected-section'),
    url(r'^delete-staff/(?P<tc>\d+)/$', deleteStaff, name='delete-staff'),
    url(r'^open-course/(?P<id>\d+)/$', openCourse, name='open-course'),
    url(r'^close-course/(?P<id>\d+)/$', closeCourse, name='close-course'),
    path('class-lists/', classLists, name="class-lists"),
    path('class-list-details/<id>/', classListDetails, name="class-list-details"),



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