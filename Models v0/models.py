from django.contrib.auth.models import User
#from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from django.db import models
from .lists import *

'''
This model is for applies. The model stores personal, contact, 
previous education and application information. The acceptance 
statue will be false as default.'''
class Visitor(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Visitors"
        verbose_name = "Visitor"

    # Personal information:
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcID = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), max_length=5, choices=sex, default='Female')

    # Contact information:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, choices=listOfCities, blank=False, default='İstanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, null=True, unique=True)

    # Previous education information:
    degree = models.CharField(('Degree'), max_length=20, choices=listOfDegree, default='Lisans')
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, default='Işık Üniversitesi')
    gpa = models.PositiveSmallIntegerField(('General Point Average'), blank=False, validators=[MaxValueValidator(4)])

    # Application information:
    referenceName = models.CharField(('Reference Name'), max_length=40, null=True, blank=False)
    referenceNamePhone = models.CharField(('Reference Phone Number'), max_length=11, blank=False, null=True)
    referenceJob = models.CharField(('Reference Job'), max_length=40, null=True, blank=False)
    referenceSector = models.CharField(('Sector'), max_length=20, choices=listOfSectors, blank=False, null=True)
    scienceExam = models.PositiveSmallIntegerField(('ALES Point'), blank=False, validators=[MaxValueValidator(100)])
    foreignLanguageExam = models.PositiveSmallIntegerField(('YDS Point'), blank=False, validators=[MaxValueValidator(100)])
    program = models.ForeignKey('Program', related_name='Program', null=True, blank=False, on_delete=models.CASCADE)

    # Acceptance Statue:
    acceptance = models.BooleanField(('Acceptance'), blank=False)

    def __str__(self):
        return self.user.first_name + str(" ") + self.user.last_name

'''This model is for students. The model receives required 
information  from relevant Visitor row. Personal, contact, 
previous education, application informations come from 
Visitor model. Also, there are going to store enstitute information.'''
class Student(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Students"
        verbose_name = "Student"

    # Personal, contact, previous education, application informations:
    student = models.OneToOneField(Visitor, on_delete=models.CASCADE, unique=True)

    # Enstitute information:
    schoolMail = models.CharField(('School Mail'), max_length=80, null=True, blank=True, unique=True)
    studentID = models.CharField(('Student ID'), max_length=9, null=True, blank=False, unique=True)
    cirriculum = models.ForeignKey(('Cirriculum'), blank=False, null=True, on_delete=models.CASCADE)
    holdState = models.BooleanField(('Hold State'), blank=False, default=False)
    regOpen = models.BooleanField(('Registration Open Statue'), blank=False, default=False)
    approvalStatue = models.BooleanField(('Approval Statue'), default=True)

    def __str__(self):
        return str(self.student) + str(" ") + str(self.studentID)

'''This model is for all staffs that are academic and institute.
It uses django-user model like Student or Visitor models. It stores
extra information. That are personal and contact informations.'''
class Staff(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Staffs"
        verbose_name = "Staff"

    # Personal information:
    staff = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcID = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)

    # Contact information:
    selfMail = models.CharField(('Self Mail'), max_length=80, null=True, blank=False, unique=True)
    schoolMail = models.CharField(('School Mail'), max_length=80, null=True, blank=True, unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, choices=listOfCities, blank=False, default='İstanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, null=True, unique=True)

    def __str__(self):
        return self.staff.first_name + str(" ") + self.staff.last_name

'''This model is for Academic Staffs. It inherits Staff model.
Also, there are some extra attributes.'''
class AcademicStaff(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Academic Staffs"
        verbose_name = "Academic Staff"

    academicStaff = models.OneToOneField(Staff, on_delete=models.CASCADE, unique=True)
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, default='Işık Üniversitesi')
    department = models.ForeignKey(('Department'), blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.academicStaff)

'''This model is for Program. It stores information about
programs. A program example is Cyber Security.'''
class Program(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Programs"
        verbose_name = "Program"

    name = models.CharField(('Name'), max_length=30, blank=False, unique=True, null=True)
    quoataManager = models.ForeignKey(('AcademicStaff'), blank=False, null=True, on_delete=models.CASCADE)
    thesis = models.BooleanField(('Thesis'), blank=True, default=False)
    phD = models.BooleanField(('Ph.D'),blank=True, default=False)

    def __str__(self):
        return self.name

'''This model is for Institute. An institute example is
Natura Science.'''
class Institute(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Institutes"
        verbose_name = "Institute"

    name = models.CharField(('Name'), max_length=30, blank=False, null=True, unique=True)
    head = models.OneToOneField(AcademicStaff, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

'''This model is for all courses. It stores all courses with
own attributes. It acts like a archieve for all defined courses.'''
class Course(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Courses"
        verbose_name = "Course"

    name = models.CharField(('Name'), max_length=30, blank=False, null=True)
    code = models.CharField(('Code'), max_length=3, blank=False, null=True, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=False, null=True)
    content = models.URLField(('PDF URL'), blank=False)
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, blank=False, null=True)
    credit = models.PositiveSmallIntegerField(('Code'), blank=False, null=True)
    ECTS = models.PositiveSmallIntegerField(('ECTS'), blank=False, null=True)
    isValid = models.BooleanField(('is Valid'), blank=True, default=False)
    deleted = models.BooleanField(('Deleted'), blank=True, default=False)

    def __str__(self):
        return self.code + str(" ") + self.name

'''This model is for completed courses. It inherits Student model.'''
class CompletedCourse(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Completed Courses"
        verbose_name = "Completed Course"

    student = models.OneToOneField(Student, on_delete=models.CASCADE, blank=False)
    ccrCourse = models.OneToOneField('CourseType', on_delete=models.CASCADE, blank=False, related_name='CompletedCourse_ccrCourse')
    actCourse = models.OneToOneField('CourseType', on_delete=models.CASCADE, blank=False, related_name='CompletedCourse_actCourse')
    grade = models.CharField(('Grade'), max_length=2, blank=False, null=True)

    def __str__(self):
        return str(self.student) + str(" ") + str(self.ccrCourse) + str(" ") + str(self.grade)

'''This model is for completed courses. It inherits Student model.'''
class TakenCourse(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Taken Courses"
        verbose_name = "Taken Course"

    student = models.OneToOneField(Student, on_delete=models.CASCADE, blank=False)
    ccrCourse = models.OneToOneField('CourseType', on_delete=models.CASCADE, blank=False)
    actCourse = models.OneToOneField('Section', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.student) + str(" ") + str(self.actCourse)

'''This model defines Schedules.'''
class Schedule(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Schedules"
        verbose_name = "Schedule"

    section = models.OneToOneField('Section', on_delete=models.CASCADE, blank=False)
    day = models.CharField(('Day'), choices=listOfDays, max_length=20, blank=False, null=True)
    slot = models.CharField(('Slot'), choices=listOfSlots, max_length=20, blank=False, null=True)
    place = models.CharField(('Place'), choices=listOfPlaces, max_length=40, blank=False, null=True)

    def __str__(self):
        return str(self.section) + str(" ") + str(self.day) + str(" ") + str(self.slot) + str(" ") + str(self.place)

'''This model defines Cirriculum for each program.
And, inherits Program model.'''
class Cirriculum(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Cirriculums"
        verbose_name = "Cirriculum"

    #courseTypes = ArrayField(models.CharField(('Course List'), max_length=500), blank=True, null=True)
    year = models.DateField(('Date'), blank=True, null=True)
    program = models.OneToOneField(Program, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.program) + str(" ") + str(self.year)

'''This model inherits Cirriculum model.'''
class CourseType(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Course Types"
        verbose_name = "Course Type"

    #course = ArrayField(models.CharField(('Course List'), max_length=500), blank=True, null=True)
    cirriculum = models.OneToOneField(Cirriculum, on_delete=models.CASCADE, blank=False)
    name = models.CharField(('Name'), max_length=10, blank=False, null=True)
    semester = models.CharField(('Semester'), max_length=1, blank=False, null=True)

    def __str__(self):
        return self.name

'''This model inherits Academic Staff model.'''
class Department(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Departments"
        verbose_name = "Department"

    name = models.CharField(('Name'), max_length=40, blank=False, null=True, unique=True)
    code = models.CharField(('Code'), max_length=3, blank=False, null=True, unique=True)
    head = models.OneToOneField(AcademicStaff, on_delete=models.CASCADE, blank=False, unique=True, related_name='Department_Head')

    def __str__(self):
        return str(self.name)

'''This model inherits Course, Academic Staff models.'''
class Section(models.Model):

    proxy = True

    class Meta:
        verbose_name_plural = "Sections"
        verbose_name = "Section"

    course = models.OneToOneField(Course, on_delete=models.CASCADE, blank=False)
    number = models.PositiveSmallIntegerField(('Number'), blank=False, null=True)
    quoata = models.PositiveSmallIntegerField(('Quoata'), blank=False, null=True)
    instructor = models.OneToOneField(AcademicStaff, blank=False, on_delete=models.CASCADE)
    year = models.CharField(('Year'), max_length=4, blank=False, null=True)
    semester = models.CharField(('Semester'), max_length=40, choices=listOfSemesters, blank=False, null=True)

    def __str__(self):
        return str(self.course) + str(" ") + str(self.number)