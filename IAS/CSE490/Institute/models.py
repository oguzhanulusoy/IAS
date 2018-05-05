from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from collections import OrderedDict
from .managers import UserManager
from .lists import *


class User(AbstractBaseUser, PermissionsMixin):

    proxy = True

    username = models.CharField(_('username'), max_length=15, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    phone_regex = RegexValidator(regex=r'^\+(?:[0-9] ?){6,14}[0-9]$',
                                 message='Phone number must be entered in the format: "+905304440044"')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    personal_information = models.ForeignKey('PersonalInformation', on_delete=models.SET_NULL, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

    class Meta:
        db_table = 'auth_user'

    def generate_unique_username(self):
        pass

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the 'real' save() method.


class Visitor(models.Model):

    proxy = True

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    tc = models.CharField('TC Number', max_length=11, unique=True)
    birthday = models.DateField('Birthday')
    gender = models.CharField('Gender', max_length=10, choices=GENDER)
    application_date = models.DateField(auto_now_add=True)
    address = models.TextField('Address', max_length=60)
    city = models.CharField('City', max_length=20, choices=CITIES)
    degree = models.CharField('Degree', max_length=10, choices=DEGREES)
    university = models.CharField('University', max_length=50, choices=UNIVERSITIES)
    gpa = models.DecimalField('GPA', decimal_places=2, max_digits=4, validators=[MinValueValidator(2),
                                                                                 MaxValueValidator(4)])
    ales = models.PositiveIntegerField('ALES', validators=[MinValueValidator(50),
                                                           MaxValueValidator(100)])
    yds = models.PositiveIntegerField('YDS', validators=[MinValueValidator(30),
                                                         MaxValueValidator(100)])
    acceptance = models.CharField('Acceptance', max_length=20, choices=ACCEPTANCE, null=True)
    program = models.ForeignKey('Program', models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class PersonalInformation(models.Model):

    proxy = True 

    id_number = models.CharField('ID Number', max_length=11, primary_key=True)
    gender = models.CharField('Gender', max_length=10, blank=True, choices=[('M', 'Male'),
                                                                            ('F', 'Female')])
    nationality = models.CharField('Nationality', max_length=15, blank=True)
    birth_date = models.DateField('Birth Date', blank=True, null=True)
    birth_place = models.CharField('Birth Place', max_length=60, blank=True)
    marital_status = models.CharField('Marital', max_length=10, blank=True, choices=[('Single', 'Single'),
                                                                                     ('Married', 'Married')],
                                      default='Single')
    religion = models.CharField('Religion', max_length=15, blank=True)
    blood_type = models.CharField('Blood Type', max_length=5, choices=[('A Rh+', 'A Rh+'),
                                                                       ('B Rh+', 'B Rh+'),
                                                                       ('AB Rh+', 'AB Rh+'),
                                                                       ('0 Rh+', '0 Rh+'),
                                                                       ('A Rh-', 'A Rh-'),
                                                                       ('B Rh-', 'B Rh-'),
                                                                       ('AB Rh-', 'AB Rh-'),
                                                                       ('0 Rh-', '0 Rh-')], blank=True)
    province = models.CharField('Province', max_length=60, blank=True)
    district = models.CharField('District', max_length=60, blank=True)
    village = models.CharField('Village', max_length=60, blank=True)
    registration_no = models.CharField('Registration No', max_length=4, blank=True)
    family_no = models.CharField('Family No', max_length=7, blank=True)
    order_no = models.CharField('Order No', max_length=4, blank=True)
    mother_name = models.CharField('Mother\'s Name', max_length=60, blank=True)
    father_name = models.CharField('Father\'s Name', max_length=60, blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.id_number

class Student(models.Model):

    proxy = True

    user = models.OneToOneField('User', models.CASCADE)
    st_id = models.CharField('Student ID', max_length=9, null=True, blank=True)
    st_email = models.EmailField('School Email Address', max_length=60, blank=True, null=True)
    curriculum = models.ForeignKey('Curriculum', models.CASCADE)
    program = models.ForeignKey('Program', models.CASCADE)
    advisor = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)
    hold_state = models.BooleanField('Hold State', default=False)
    reg_open_statue = models.BooleanField('Registration Open Statue', default=False)
    approval_statue = models.BooleanField('Approval Statue', default=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class Staff(models.Model):

    proxy = True

    user = models.OneToOneField('User', models.CASCADE)
    tc = models.CharField('TC Number', max_length=11, unique=True)
    birthday = models.DateField('Birthday')
    gender = models.CharField('Gender', max_length=10, choices=GENDER)
    joined_date = models.DateField(auto_now_add=True)
    main_email = models.EmailField('Main Email', unique=True)
    school_email = models.EmailField('School Email', unique=True)
    address = models.TextField('Address', max_length=60, null=True, blank=False)
    city = models.CharField('City', max_length=20, choices=CITIES)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class AcademicStaff(models.Model):

    proxy = True

    staff = models.OneToOneField('Staff', models.CASCADE)
    university = models.CharField('University', max_length=60, choices=UNIVERSITIES, default='Işık Üniversitesi')
    institute = models.ForeignKey('Institute', models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['staff']

    @property
    def first_name(self):
        return self.staff.user.first_name

    @property
    def last_name(self):
        return self.staff.user.last_name

    def __str__(self):
        return str(self.staff)

class Institute(models.Model):

    proxy = True

    name = models.CharField('Institute Name', max_length=60)
    head = models.ForeignKey('AcademicStaff', models.SET_NULL, related_name='inst_head', blank=True, null=True)
    establishedDate = models.DateField('established date')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Department(models.Model):

    proxy = True

    name = models.CharField('Name', max_length=60)
    institute = models.ForeignKey('Institute', models.CASCADE)
    head = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class QuotaManager(models.Model):

    proxy = True

    quota_manager = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.quota_manager.staff.user.first_name)+" "+str(self.quota_manager.staff.user.last_name)

# ALİ'NİN MODELDE QUOTA_MANAGER FOREIGN KEY'İ QUOTA MANAGER DEĞİL, ACADEMIC STAFF
class Program(models.Model):

    proxy = True

    name = models.CharField('Name', max_length=60)
    code = models.CharField('Code', max_length=4)
    type = models.CharField('Type', max_length=60, choices=PROGRAM_TYPES)
    thesis = models.BooleanField('Thesis', default=False)
    department = models.ForeignKey(Department, models.CASCADE)
    head = models.ForeignKey('AcademicStaff', models.SET_NULL, related_name='prog_head', blank=True, null=True)
    quota_manager = models.ForeignKey('QuotaManager', models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ['code', 'type', 'thesis']
        ordering = ['type', 'name']

    def __str__(self):
        if self.thesis:
            return self.name + ' (With Thesis)'
        return self.name + ' (Without Thesis)'

    def get_absolute_url(self):
        return "/program-details/%s/" %(self.id)

class Curriculum(models.Model):

    proxy = True

    program = models.ForeignKey('Program', models.CASCADE, verbose_name='Program', blank=False)
    year = models.PositiveIntegerField(verbose_name='Year', blank=False,
                                       validators=[MinValueValidator(2000),
                                                   MaxValueValidator(datetime.now().year + 1)])
    class Meta:
        ordering = ['program', 'year']

    def __str__(self):
        return self.program.name + ' Program ' + str(self.year) + ' Curriculum'


class Course(models.Model):

    proxy = True

    code = models.CharField('Course Code', max_length=3, unique=True)
    title = models.CharField('Course Title', max_length=60, blank=False)
    description = models.TextField('Course Description', max_length=255, blank=True)
    credit = models.IntegerField('Course Credit', blank=False)
    ects_credit = models.IntegerField('Course ECTS Credit', blank=False)
    program = models.ForeignKey('Program', models.CASCADE)
    university = models.CharField('University', max_length=60, choices=UNIVERSITIES, default='Işık Üniversitesi')
    is_valid = models.BooleanField('Is Valid', default=False)
    is_deleted = models.BooleanField('Deleted', default=False)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['program', 'code']

    def __str__(self):
        return self.title

class Section(models.Model):

    proxy = True

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    number = models.PositiveIntegerField('Section Number', validators=[MinValueValidator(1)])
    quota = models.PositiveIntegerField('Quota Quanitity', validators=[MaxValueValidator(50)], null=True)
    instructor = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)
    year = models.CharField('Year', max_length=4, default=datetime.now().year)
    semester = models.CharField('Semester', max_length=10, choices=SEMESTERS)
    special_quota = models.ManyToManyField(Student, blank=True, null=True, related_name='special_quota')
    students = models.ManyToManyField(Student, blank=True, null=True, related_name='students')

    def __str__(self):
        if self.number < 10:
            return self.course.code + '.0' + str(self.number)
        return self.course.code + str(self.number)

    class Meta:
        unique_together = ('course', 'number')
        ordering = ('course', 'number')

class Schedule(models.Model):

    proxy = True

    section = models.ForeignKey('Section', verbose_name='Section', max_length=10, on_delete=models.CASCADE)
    day = models.CharField('Section Day', max_length=15, choices=DAYS)
    slot = models.CharField('Section Slot', max_length=2, choices=SLOTS)
    place = models.CharField('Place', max_length=15, choices=PLACES)

    def __str__(self):
        return '(' + str(self.section) + ') ' + str(self.day) + str(self.slot) + ' / ' + self.place

    class Meta:
        verbose_name = 'Course Schedule'
        unique_together = ['section', 'day', 'slot']
        ordering = ['section', 'day', 'slot']

def write_roman(num):
    roman = OrderedDict()
    roman[10] = 'X'
    roman[9] = 'IX'
    roman[5] = 'V'
    roman[4] = 'IV'
    roman[1] = 'I'

    def roman_num(number):
        for r in roman.keys():
            x, y = divmod(number, r)
            yield roman[r] * x
            number -= (r * x)
            if number > 0:
                roman_num(number)
            else:
                break

    return ''.join([a for a in roman_num(num)])

class CourseType(models.Model):

    proxy = True

    title = models.CharField('Title', max_length=60)
    code = models.CharField('Code', max_length=15, unique=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return str(self.code)


class CcrCourse(models.Model):

    proxy = True

    curriculum = models.ForeignKey('Curriculum', models.CASCADE)
    type = models.ForeignKey('CourseType', models.CASCADE)
    no = models.PositiveIntegerField('Course Number', validators=[MinValueValidator(1)], default=1)
    semester = models.PositiveIntegerField('Semester', validators=[MinValueValidator(1),
                                                                   MaxValueValidator(10)])

    class Meta:
        unique_together = ('curriculum', 'type', 'no')
        ordering = ['curriculum', 'type', 'no', 'semester']

    def __str__(self):
        return str(self.curriculum.program.code) + '_' + str(self.type.code) \
               + "-" + str(write_roman(self.no))

class OfferedCourse(models.Model):

    proxy = True

    ccr_course = models.ForeignKey('CcrCourse', models.CASCADE)
    act_course = models.ForeignKey('Course', models.CASCADE)

    class Meta:
        unique_together = ['ccr_course', 'act_course']

    def __str__(self):
        return str(self.ccr_course.ccr.program.code) + '_' + str(self.ccr_course.type) \
               + " -> " + str(self.act_course)

class TakenCourse(models.Model):

    proxy = True

    student = models.ForeignKey('Student', models.CASCADE)
    ccr_course = models.ForeignKey('CcrCourse', models.CASCADE)
    act_course = models.ForeignKey('Section', models.CASCADE)
    accepted = models.NullBooleanField('Acceptance', default=False)

    class Meta:
        verbose_name = 'Taken Course'
        unique_together = ['student', 'ccr_course', 'act_course']

    def __str__(self):
        return str(self.student)+ ' ' +str(self.act_course.course.title)

class CompletedCourse(models.Model):

    proxy = True
    
    student = models.ForeignKey('Student', models.CASCADE)
    ccr_course = models.ForeignKey('CcrCourse', models.CASCADE)
    act_course = models.ForeignKey('Course', models.CASCADE)
    grade = models.CharField('Grade', max_length=2)

    class Meta:
        verbose_name = 'Completed Course'
        verbose_name_plural = 'Completed Courses'
        unique_together = ['student', 'ccr_course', 'act_course']

    def __str__(self):
        return str(self.student) + ' ' + str(self.ccr_course) + ' ' + str(self.grade)
