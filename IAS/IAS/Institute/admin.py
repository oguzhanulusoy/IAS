from django.contrib import admin
from .models import *

class AcademicInstructorAdmin(admin.ModelAdmin):
    search_fields = ["firstName", "middleName", "lastName", "joinedDate", "tcNumber", "birthday", "gender", "mail", "city", "phoneNumber", "ssn"]
    list_display = ["firstName", "lastName", "joinedDate", "tcNumber", "phoneNumber", "mail"]

admin.site.register(AcademicInstructor, AcademicInstructorAdmin)

class GrandStudentAdmin(admin.ModelAdmin):
    list_display = ["studentID", "firstName", "lastName", "tcNumber", "program", "mail", "phoneNumber", "startingDate"]
    list_filter = ["gpaI", "city", "program", "academicSupervisior", "semester", "scholarship", "startingDate"]
    search_fields = ["gpa", "scienceExam", "foreignLanguageExam", "program", "city", "degree", "university",
                     "firstName", "lastName", "tcNumber", "mail", "studentID", "academicSupervisior", "semester", "scholarship", "startingDate"]

admin.site.register(GrandStudent, GrandStudentAdmin)

admin.site.register(Instructor)

class InstituteStaffAdmin(admin.ModelAdmin):
    search_fields = ["firstName", "middleName", "lastName", "joinedDate", "tcNumber", "birthday", "gender", "mail", "address", "city", "phoneNumber"]
    list_display = ["firstName", "lastName", "joinedDate", "phoneNumber", "mail"]

admin.site.register(InstituteStaff, InstituteStaffAdmin)

class ApplyAdmin(admin.ModelAdmin):
    list_display = ["firstName", "lastName", "tcNumber", "gpa", "scienceExam", "foreignLanguageExam", "program"]
    list_filter = ["gpa", "scienceExam", "foreignLanguageExam", "program", "city", "degree", "university"]
    search_fields = ["gpa", "scienceExam", "foreignLanguageExam", "program", "city", "degree", "university", "firstName", "lastName", "tcNumber", "mail"]

admin.site.register(Apply, ApplyAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["code", "definition", "head"]

admin.site.register(Department, DepartmentAdmin)

class ProgramAdmin(admin.ModelAdmin):
    search_fields = ["department", "name"]
    list_filter = ["department"]
    list_display = ["department", "name"]

admin.site.register(Program, ProgramAdmin)

class HeadAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Head, HeadAdmin)

class CourseAdmin(admin.ModelAdmin):
    search_fields = ["program", "code", "definition", "date", "instructor", "credit"]
    list_filter = ["program", "date", "instructor"]
    list_display = ["date", "program", "definition"]

admin.site.register(Course, CourseAdmin)

class TakenCourseAdmin(admin.ModelAdmin):
    search_fields = ["program", "course"]
    list_display = ["program", "course"]
    list_filter = ["program", "course"]

admin.site.register(TakenCourse, TakenCourseAdmin)

class OpenCourseAdmin(admin.ModelAdmin):
    search_fields = ["program", "course"]
    list_display = ["program", "course"]
    list_filter = ["program", "course"]

admin.site.register(OpenCourse, OpenCourseAdmin)

class FormAdmin(admin.ModelAdmin):
    search_fields = ["formID", "title", "description", "link"]
    list_display = ["formID", "title"]

admin.site.register(Form, FormAdmin)

class ReportAdmin(admin.ModelAdmin):
    search_fields = ["reportID", "title", "content","link"]
    list_display = ["reportID", "title"]

admin.site.register(Report, ReportAdmin)

admin.site.register(Supervisior)

class WeeklyScheduleIAdmin(admin.ModelAdmin):
    search_fields = ["instructorID", "course"]
    list_display = ["course", "instructorID"]
    list_filter = ["course", "instructorID"]

admin.site.register(WeeklyScheduleI)

class WeeklyScheduleSAdmin(admin.ModelAdmin):
    search_fields = ["studentID", "course"]
    list_display = ["course", "studentID"]
    list_filter = ["course", "studentID"]

admin.site.register(WeeklyScheduleS, WeeklyScheduleSAdmin)

class ClassesAdmin(admin.ModelAdmin):
    search_fields = ["className", "days"]
    list_display = ["days", "className"]
    list_filter = ["className"]
    #editable fields

admin.site.register(Classes, ClassesAdmin)

class PushNotificationIStoInstructorsAdmin(admin.ModelAdmin):
    search_fields = ["institute", "instructors", "subject", "text"]
    list_display = ["institute", "subject"]
    list_filter = ["institute", "instructors"]

admin.site.register(PushNotificationIStoInstructors, PushNotificationIStoInstructorsAdmin)

class PushNotificationIStoStudentsAdmin(admin.ModelAdmin):
    search_fields = ["institute", "grandStudents", "subject", "text"]
    list_display = ["institute", "subject"]
    list_filter = ["institute", "grandStudents"]

admin.site.register(PushNotificationIStoStudents, PushNotificationIStoStudentsAdmin)

class PushNotificationAItoStudentsAdmin(admin.ModelAdmin):
    search_fields = ["instructor", "grandStudents", "text", "subject"]
    list_display = ["instructor", "subject"]
    list_filter = ["instructor"]

admin.site.register(PushNotificationAItoStudents, PushNotificationAItoStudentsAdmin)

admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(Semester)

admin.site.register(RequestOpenCourse)

admin.site.register(BuildingSchema)

admin.site.register(CCR)
