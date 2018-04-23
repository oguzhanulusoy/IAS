from django.contrib import admin
from .models import *


class VisitorAdmin(admin.ModelAdmin):
    readonly_fields = ('accepted',)


class TakenCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'ccr_course', 'act_course')


class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['year']


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'code']


class CompletedCourseAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Curriculum)
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Section, SectionAdmin)
admin.site.register(Schedule)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(CcrCourse)
admin.site.register(OfferedCourse)
admin.site.register(TakenCourse, TakenCourseAdmin)
admin.site.register(CompletedCourse, CompletedCourseAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitorProgram)
admin.site.register(User)
admin.site.register(AcademicStaff)
admin.site.register(Student)
admin.site.register(Institute)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(PersonalInformation)

