from django import forms
from .models import *

# DEPARTMENT
class AddDepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = '__all__'

# PROGRAM
class AddProgramForm(forms.ModelForm):
	class Meta:
		model = Program
		fields = '__all__'

# CURRICULUM
class AddCirriculumForm(forms.ModelForm):
	class Meta:
		model = Curriculum
		fields = '__all__'

# INSTITUTE
class AddInstituteForm(forms.ModelForm):
	class Meta:
		model = Institute
		fields = '__all__'

# COURSE
class AddCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		exclude = ['is_valid', 'is_deleted', 'created_date']

# COURSE TYPE
class AddCourseTypeForm(forms.ModelForm):
	class Meta:
		model = CourseType
		fields = '__all__'

# SECTION
class AddSectionForm(forms.ModelForm):
	class Meta:
		model = Section
		exclude = ['year']

# QUOTA-MANAGER
class AddQuoataManagerForm(forms.ModelForm):
	class Meta:
		model = QuotaManager
		fields = '__all__'

# ACADEMIC STAFF
class AddAcademicStaffForm(forms.ModelForm):
	class Meta:
		model = AcademicStaff
		fields = '__all__'

# STAFF
class AddStaffForm(forms.ModelForm):
	class Meta:
		model = Staff
		exclude = ['user']
		#fields = '__all__'

# VISITOR
class AddVisitorForm(forms.ModelForm):
	class Meta:
		model = Visitor
		exclude = ['user','acceptance']

# STUDENT
class AddStudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['user']

# USER
class AddUserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ['last_login', 'groups', 'user_permissions', 'is_active', 'is_superuser', 'is_staff']

# EDIT COURSE (OPEN)
class EditCourseForm(forms.ModelForm):
	editted_date = forms.DateField()
	class Meta:
		model = Course
		fields = ['is_valid']

# REMOVE COURSE (CLOSE)
class RemoveCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['is_deleted']



