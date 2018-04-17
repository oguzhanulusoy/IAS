from django import forms
from .models import *

class AddDepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = '__all__'

class AddProgramForm(forms.ModelForm):
	class Meta:
		model = Program
		fields = '__all__'

class AddCirriculumForm(forms.ModelForm):
	class Meta:
		model = Curriculum
		fields = '__all__'

class AddCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		exclude = ['is_valid', 'is_deleted', 'created_date']

class AddCourseTypeForm(forms.ModelForm):
	class Meta:
		model = CourseType
		fields = '__all__'

class AddSectionForm(forms.ModelForm):
	class Meta:
		model = Section
		exclude = ['year']

class AddAcademicStaffForm(forms.ModelForm):
	class Meta:
		model = AcademicStaff
		exclude = ['staff']

class AddStaffForm(forms.ModelForm):
	class Meta:
		model = Staff
		exclude = ['user']

class AddUserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ['password', 'password1', 'user_permissions', 'last_login', 
		'personal_information', 'avatar', 'is_active', 'is_superuser', 'groups']

		def signup(self, request, user):
			password = str(User.objects.make_random_password())
			user.set_password(password)  
			user.save()



