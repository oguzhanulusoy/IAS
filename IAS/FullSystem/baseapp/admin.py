from django.contrib import admin
from .models import *


class VisitorAdmin(admin.ModelAdmin):
    readonly_fields = ('accepted',)


class CcrCourseAdmin(admin.ModelAdmin):
    exclude = ('no',)


class TakenCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'ccr_course', 'act_course')


class SectionAdmin(admin.ModelAdmin):
    exclude = ('number', 'year',)


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'code']


class CompletedCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'ccr_course', 'act_course', 'grade')


# Register your models here.
admin.site.register(Curriculum)
admin.site.register(Course)
admin.site.register(Section, SectionAdmin)
admin.site.register(Schedule)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(CcrCourse, CcrCourseAdmin)
admin.site.register(OfferedCourse)
admin.site.register(TakenCourse, TakenCourseAdmin)
admin.site.register(CompletedCourse, CompletedCourseAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitorProgram)
admin.site.register(User)
admin.site.register(AcademicStaff)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Institute)
admin.site.register(Department)
admin.site.register(Program)


#### YENi EKLENENLER ####
admin.site.register(ExamDate)
admin.site.register(MakeAnnouncement)

