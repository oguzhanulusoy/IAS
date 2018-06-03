from django import forms
from .lists import *
from .models import Program, Institute, Department
from .models import User, Student, Visitor, Staff, AcademicStaff, PersonalInformation
from .models import Section, CompletedCourse, TakenCourse, Course, CourseType, Curriculum

text_widget = forms.TextInput(attrs={'class': 'form-control'})
password_widget = forms.PasswordInput(attrs={'class': 'form-control'})
radio_widget = forms.Select(attrs={'class': 'form-control'})
choice_widget = forms.Select(attrs={'class': 'form-control'})
program_choice_widget = forms.SelectMultiple(attrs={'class': 'form-control'})
area_widget = forms.Textarea(attrs={'class': 'form-control'})


# Ömer Berkhan - Burak Sağlam

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class ApplicationForm(forms.Form):
    tc = forms.CharField(label='TC', max_length=11, required=True, widget=text_widget)
    first_name = forms.CharField(label='First Name', max_length=60, required=True, widget=text_widget)
    last_name = forms.CharField(label='Last Name', max_length=30, required=True, widget=text_widget)
    email = forms.EmailField(label='E-Mail', required=True, widget=text_widget)
    phone_number = forms.CharField(label='Phone Number', max_length=14, required=True, widget=text_widget)
    birthday = forms.DateField(label='Birthday', required=True, widget=text_widget, input_formats=['%d-%m-%Y'])
    gender = forms.ChoiceField(label='Gender', required=True, widget=radio_widget, choices=GENDER)
    address = forms.CharField(label='Address', max_length=150, required=True, widget=area_widget)
    city = forms.ChoiceField(label='City', required=True, widget=choice_widget, choices=CITIES)
    degree = forms.ChoiceField(label='Degree', required=True, widget=choice_widget, choices=DEGREES)
    university = forms.ChoiceField(label='University', required=True, widget=choice_widget, choices=UNIVERSITIES)
    gpa = forms.DecimalField(label='GPA', required=True, widget=text_widget, max_digits=4, decimal_places=2)
    ales = forms.IntegerField(label='ALES', required=True, widget=text_widget)
    yds = forms.IntegerField(label='YDS', required=True, widget=text_widget)
    program = forms.ModelMultipleChoiceField(label='Program', required=True, widget=program_choice_widget,
                                             queryset=Program.objects.all())


class PersonalInformationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonalInformationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PersonalInformation
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.TextInput(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_type': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_no': forms.TextInput(attrs={'class': 'form-control'}),
            'family_no': forms.TextInput(attrs={'class': 'form-control'}),
            'order_no': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Muhammed Ali


class QuotaChangeForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = {
            'quota',
        }


class AddNewSection(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class Grade2Student(forms.ModelForm):
    class Meta:
        model = CompletedCourse
        fields = ['grade', 'act_course']


class OpenNewSection(forms.ModelForm):
    class Meta:
        model = Section

        exclude = ['special_quota', 'students', 'year']


class ScheduleApproveOrReject(forms.ModelForm):
    class Meta:
        model = TakenCourse

        fields = '__all__'


# Oğuz

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
    # fields = '__all__'


# VISITOR
class AddVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        exclude = ['user', 'acceptance']


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
