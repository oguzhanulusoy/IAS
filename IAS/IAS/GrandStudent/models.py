from django.db import models
from django.core.validators import MaxValueValidator

# mezuniyet dereceleri:
listOfDegree = (('Lisans', 'LISANS'),
                ('Yuksek Lisans', 'YUKSEK LISANS'),
                ('Doktora', 'DOKTORA'))

# okul listesi:
listOfUniversities = (('FMV Isik University', 'FMV ISIK UNIVERSITY'),
                      ('Galatasaray University', 'GALATASARAY UNIVERSITY'))

# program listesi:
listOfPrograms = (('cse', 'CSE'), ('se', 'SE'))

# cinsiyet listesi:
sex = (('kadın', 'KADIN'), ('erkek', 'ERKEK'))

# pre-registration:
class Apply(models.Model):
    # Kimlik bilgileri:
    firstName = models.CharField(('First Name'), max_length=15, blank=False)
    middleName = models.CharField(('Middle Name'), max_length=15, blank=True)
    lastName = models.CharField(('Last Name'), max_length=15, blank=False)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcNumber = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), max_length=5, choices=sex, default='Kadın')

    # İletişim bilgileri:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, blank=False)
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='00000000000', unique=True)

    # Başvuru bilgileri:
    degree = models.CharField(('Degree'), max_length=20, choices=listOfDegree, default='Lisans')
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, default='Galatasaray University')
    gpa = models.PositiveSmallIntegerField(('General Point Average'), blank=False, validators=[MaxValueValidator(4)])
    scienceExam = models.PositiveSmallIntegerField(('ALES Point'), blank=False, validators=[MaxValueValidator(100)])
    foreignLanguageExam = models.PositiveSmallIntegerField(('YDS Point'), blank=False, validators=[MaxValueValidator(100)])
    program = models.CharField(('Program'), max_length=40, choices=listOfPrograms, default='cse')

# registration:
class PersonalInformation(models.Model):
    # Kimlik bilgileri:
    firstName = models.CharField(('First Name'), max_length=15, blank=False)
    middleName = models.CharField(('Middle Name'), max_length=15, blank=True)
    lastName = models.CharField(('Last Name'), max_length=15, blank=False)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcNumber = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), default='kadın', max_length=5, choices=sex)

    # İletişim bilgileri:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, blank=False, default='Istanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='00000000000', unique=True)

    # Başvuru bilgileri:
    degree = models.CharField(('Degree'), max_length=20, choices=listOfDegree, default='Lisans')
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, default='Galatasaray University')
    gpa = models.PositiveSmallIntegerField(('General Point Average'), blank=False, validators=[MaxValueValidator(4)])
    scienceExam = models.PositiveSmallIntegerField(('ALES Point'), blank=False, validators=[MaxValueValidator(100)])
    foreignLanguageExam = models.PositiveSmallIntegerField(('YDS Point'), blank=False, validators=[MaxValueValidator(100)])

    # Enstitü bilgileri:
    program = models.CharField(('Program'), max_length=40, choices=listOfPrograms, default='cse')
    academicSupervisior = models.CharField(('Academic Supervisior'), max_length=50)
    semester = models.PositiveSmallIntegerField(('Statue'), blank=False, validators=[MaxValueValidator(4)])
    scholarship = models.PositiveSmallIntegerField(('Scholarship'), validators=[MaxValueValidator(100)])
    studentID = models.CharField(('Student ID'), max_length=9)
    startingDate = models.DateField(('Starting Date'), default='2018-03-23')
    endingDate = models.DateField(('Ending Date'), default='2018-03-23')
    gpaI = models.PositiveSmallIntegerField(('GPA'), validators=[MaxValueValidator(4)], default='0')
    completedCredit = models.CharField(('Completed Credit'), default='0', max_length=3)

class AllCourses(models.Model):
    courseCode = models.CharField(('Course Code'), max_length=6, default='null', blank=False)
    courseName = models.CharField(('Course Name'), max_length=50, default='null', blank=False)
    courseCredit = models.PositiveSmallIntegerField(('Course Credit'), validators=[MaxValueValidator(5)], default='0', blank=False)
    department = models.CharField(('Department'), max_length=4, default='null', blank=False)
    definition = models.CharField(('Definition'), max_length=500, default='null', blank=False)

class OpenCourses(models.Model):
    courseCode = models.CharField(('Course Code'), max_length=6, default='null', blank=False)
    courseName = models.CharField(('Course Name'), max_length=50, default='null', blank=False)
    courseCredit = models.PositiveSmallIntegerField(('Course Credit'), validators=[MaxValueValidator(5)], default='0', blank=False)
    department = models.CharField(('Department'), max_length=4, default='null', blank=False)
    courseClass = models.CharField(('Course Class'), max_length=10, default='null', blank=False)
    courseDescription = models.CharField(('Course Description'), max_length=500, default='null', blank=False)
    courseInstructor = models.CharField(('Course Instructor'), max_length=50, default='null', blank=True) #hoca atanmamış olabilir
    year = models.PositiveSmallIntegerField(('Year'), default='2018', blank=False)

class TakenCourses(models.Model):
    lectures = models.FileField(('File field'), max_length=10)