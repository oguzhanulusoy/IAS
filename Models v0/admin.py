from django.contrib import admin
from .models import *

class VisitorAdmin(admin.ModelAdmin):
    list_filter = ["city", "degree", "university", "gpa", "scienceExam", "foreignLanguageExam", "program"]
    list_display = ["tcID","user", "mail", "gpa", "scienceExam", "foreignLanguageExam", "acceptance"]
    search_fields = ["city", "user", "degree", "university", "gpa", "scienceExam", "foreignLanguageExam", "program", "tcID", "mail", "acceptance"]

admin.site.register(Visitor, VisitorAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_filter = ["student", "schoolMail", "studentID", "cirriculum", "holdState", "regOpen", "approvalStatue"]
    list_display = ["studentID", "student", "schoolMail", "cirriculum", "holdState", "regOpen"]
    search_fields = ["student", "schoolMail", "studentID", "cirriculum", "holdState", "regOpen", "approvalStatue"]

admin.site.register(Student, StudentAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_filter = ["course", "number", "instructor", "year", "semester"]
    search_fields = ["course", "number", "instructor", "year", "semester"]
    list_display = ["year", "semester", "course", "number", "instructor", "quoata"]

admin.site.register(Section, SectionAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "head"]
    search_fields = ["name", "code", "head"]

admin.site.register(Department, DepartmentAdmin)

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "semester", "cirriculum"]
    search_fields = ["name", "semester", "cirriculum"]

admin.site.register(CourseType, CourseTypeAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "department", "isValid"]
    list_filter = ["department", "isValid", "deleted", "university"]
    search_fields = ["department", "isValid", "deleted", "university", "credit", "content", "name", "code"]

admin.site.register(Course, CourseAdmin)

class CirriculumAdmin(admin.ModelAdmin):
    list_display = ["year", "program"]

admin.site.register(Cirriculum, CirriculumAdmin)

class InstituteAdmin(admin.ModelAdmin):
    list_display = ["name", "head"]

admin.site.register(Institute, InstituteAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["section", "day", "slot" ,"place"]
    list_filter = ["section", "day", "slot" ,"place"]
    search_fields = ["section", "day", "slot" ,"place"]

admin.site.register(Schedule, ScheduleAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ["tcID", "staff", "phoneNumber", "selfMail", "joinedDate"]
    list_filter = ["joinedDate"]
    search_fields = ["tcID", "staff", "phoneNumber", "selfMail", "joinedDate", "birthday", "schoolMail", "city", "address"]

admin.site.register(Staff, StaffAdmin)

class AcademicStaffAdmin(admin.ModelAdmin):
    list_display = ["academicStaff", "university", "department"]
    search_fields = ["academicStaff", "university", "department"]

admin.site.register(AcademicStaff, AcademicStaffAdmin)

class TakenCourseAdmin(admin.ModelAdmin):
    list_display = ["student", "ccrCourse", "actCourse"]
    search_fields = ["student"]

admin.site.register(TakenCourse, TakenCourseAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "quoataManager", "thesis", "phD"]
    search_fields = ["name", "quoataManager", "thesis", "phD"]
    list_filter = ["name", "quoataManager", "thesis", "phD"]

admin.site.register(Program, ProgramAdmin)

admin.site.register(CompletedCourse)