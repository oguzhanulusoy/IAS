from django.contrib import admin
from .models import PersonalInformation, Apply, AllCourses, OpenCourses

# Register your models here.

admin.site.register(PersonalInformation)
admin.site.register(Apply)
admin.site.register(AllCourses)
admin.site.register(OpenCourses)