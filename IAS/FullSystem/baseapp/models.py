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
from .rules import *


class User(AbstractBaseUser, PermissionsMixin):
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
    avatar = models.ImageField(upload_to='media/avatars/', null=True, blank=True, default='avatars/ppic.png')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

    class Meta:
        db_table = 'auth_user'

    @classmethod
    def create(cls, first_name, last_name, email, phone_number, password):
        return cls(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                   password=password)

    @property
    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_type(self):
        try:
            return self.student.__class__
        except Student.DoesNotExist:
            try:
                return self.staff.academicstaff.__class__
            except AcademicStaff.DoesNotExist:
                return self.staff.__class__



    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Visitor(models.Model):
    # Personal Information
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    tc = models.CharField('TC Number', max_length=11, unique=True)
    birthday = models.DateField('Birthday')
    gender = models.CharField('Gender', max_length=10, choices=GENDER)
    application_date = models.DateField(auto_now_add=True)

    # Contact Information
    address = models.TextField('Address', max_length=60)
    city = models.CharField('City', max_length=20, choices=CITIES)

    # Previous Education Information
    degree = models.CharField('Degree', max_length=10, choices=DEGREES)
    university = models.CharField('University', max_length=50, choices=UNIVERSITIES)
    gpa = models.DecimalField('GPA', decimal_places=2, max_digits=4, validators=[MinValueValidator(2),
                                                                                 MaxValueValidator(4)])

    program = models.ForeignKey('Program', models.CASCADE, blank=False, null=True)

    # Exam Information
    ales = models.PositiveIntegerField('ALES', validators=[MinValueValidator(50),
                                                           MaxValueValidator(100)])
    yds = models.PositiveIntegerField('YDS', validators=[MinValueValidator(30),
                                                         MaxValueValidator(100)])

    # Acceptance Status
    accepted = models.BooleanField('Accepted', default=False)

    is_deleted = models.BooleanField('Deleted', default=False)

    @classmethod
    def create(cls, user, tc, birthday, gender, address, city, degree, university, gpa, ales, yds):
        return cls(user=user, tc=tc, birthday=birthday, gender=gender, address=address, city=city, degree=degree,
                   university=university, gpa=gpa, ales=ales, yds=yds, accepted=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class VisitorProgram(models.Model):
    visitor = models.ForeignKey('Visitor', models.CASCADE)
    program = models.ForeignKey('Program', models.CASCADE)

    class Meta:
        unique_together = ['visitor', 'program']

    @classmethod
    def create(cls, visitor, program):
        return cls(visitor=visitor, program=program)

    def __str__(self):
        return str(self.visitor) + ' -> ' + str(self.program)


class PersonalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_number = models.CharField('ID Number', max_length=11)
    gender = models.CharField('Gender', max_length=10, blank=True, choices=GENDER)
    nationality = models.CharField('Nationality', max_length=15, blank=True)
    birth_date = models.DateField('Birth Date', blank=True, null=True)
    birth_place = models.CharField('Birth Place', max_length=60, blank=True)
    marital_status = models.CharField('Marital', max_length=10, blank=True, choices=MARITAL_STATUS,
                                      default='Single')
    religion = models.CharField('Religion', max_length=15, blank=True)
    blood_type = models.CharField('Blood Type', max_length=5, choices=BLOOD_TYPES, blank=True)
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
        return self.user


class Student(models.Model):
    user = models.OneToOneField('User', models.CASCADE)
    st_email = models.EmailField('School Email Address', max_length=60, blank=True, null=True)
    st_id = models.CharField('Student ID', max_length=9, null=True, blank=True)

    program = models.ForeignKey('Program', models.CASCADE)
    advisor = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)
    curriculum = models.ForeignKey('Curriculum', models.CASCADE, null=True)
    hold_state = models.BooleanField('Hold State', default=False)
    reg_open_statue = models.BooleanField('Registration Open Statue', default=False)
    approval_statue = models.BooleanField('Approval Statue', default=True)

    class Meta:
        ordering = ['user']

    def add_taken_course(self, ccr_course_id, act_course_id):
        try:
            student_ccr_courses = self.program.get_curriculum().get_courses()

            ccr_course = CcrCourse.objects.get(pk=ccr_course_id)
            act_course = Section.objects.get(pk=act_course_id)

            taken_courses = self.get_taken_courses()
            completed_courses = self.get_completed_courses()

            if act_course.quota <= 0:
                raise Exception('There is not enough quota for this section!')

            if ccr_course not in student_ccr_courses:
                raise Exception('This course type not valid for your curriculum!')

            for offered_course in ccr_course.get_offered_courses():
                exists = False
                if act_course in offered_course.sections:
                    exists = True
                if not exists:
                    raise Exception('This course not offered for selected course type!')
            for taken_course in taken_courses:
                if taken_course.act_course == act_course or taken_course.ccr_course == ccr_course:
                    raise Exception('This course already selected!')
            for completed_course in completed_courses:
                if completed_course.act_course == act_course or completed_course.ccr_course == ccr_course:
                    if grade_point(completed_course.grade) >= 2:
                        raise Exception('This course completed before!')

            act_course.quota -= 1
            act_course.save()

            taken_course = TakenCourse(student=self, ccr_course=ccr_course, act_course=act_course)
            taken_course.save()

            return True
        except Exception as e:
            return e

    def get_next_lecture(self):
        taken_courses = self.get_taken_courses()

        schedules = []
        for course in taken_courses:
            schedule = list(course.act_course.get_schedule())
            if schedule:
                for section in schedule:
                    schedules.append(section)

        if not len(schedules):
            return None

        schedules.sort(key=lambda sch: sch.day * 100 + sch.slot)

        now = datetime.now()
        day = int(now.strftime('%u'))
        hour = int(now.strftime('%H'))
        slot = hour - 8
        now_value = day * 100 + slot
        lecture = schedules[0]
        for sch in schedules:
            value = int(sch.day) * 100 + int(sch.slot)
            if value > now_value:
                lecture = sch
                break

        return {
            'section': lecture.section,
            'day': DAYS[int(lecture.day) - 1][1],
            'hour': SLOTS[int(lecture.slot) - 1][1].split('-')[0] + str('.00'),
            'place': PLACES[int(lecture.place) - 1][1]
        }

    def get_curriculum(self):
        ccr = self.program.get_curriculum()

        ccr_courses = list(ccr.get_courses())
        completed_courses = list(self.get_completed_courses())
        taken_courses = list(self.get_taken_courses())

        ccr_courses.sort(key=lambda x: x.semester)

        class StudentCcr:
            def __init__(self, id, code, title, credit, semester, taken=False, completed=False, other=None):
                self.id = id
                self.code = code
                self.title = title
                self.credit = credit
                self.semester = semester
                self.taken = taken
                self.completed = completed
                self.other = other

        courses = {}
        for ccr_course in ccr_courses:
            id = ccr_course.id
            code = ccr_course.code
            title = ccr_course.title
            credit = ccr_course.credit
            semester = ccr_course.semester

            st_ccr = StudentCcr(id, code, title, credit, semester)

            if semester in courses.keys():
                semester_courses = courses.get(semester)
            else:
                courses[semester] = []
                semester_courses = courses.get(semester)

            semester_courses.append(st_ccr)

            if ccr_course in taken_courses:
                for taken_course in taken_courses:
                    if ccr_course == taken_course:
                        st_ccr.taken = True
                        st_ccr.other = taken_course

            if ccr_course in completed_courses:
                for completed_course in completed_courses:
                    if ccr_course == completed_course:
                        st_ccr.other = completed_course
                        if grade_point(completed_course.grade) >= 2 and ccr_course not in taken_courses:
                            st_ccr.completed = True

        return courses

    def get_schedule(self):
        taken_courses = self.get_taken_courses()

        days_schedule = {}
        for day in DAYS:
            day_slots = []
            for i in range(len(SLOTS)):
                day_slots.append([])
            days_schedule[day[1]] = day_slots

        for taken_course in taken_courses:
            schedule = taken_course.act_course.get_schedule()
            for sch in schedule:
                days_schedule.get(DAYS[int(sch.day) - 1][1])[int(sch.slot) - 1].append(sch)

        return days_schedule

    def get_completed_courses(self):
        return CompletedCourse.objects.filter(student=self)

    def get_completed_credit(self):
        completed_courses = self.get_completed_courses()
        credit = 0
        for course in completed_courses:
            credit += course.credit
        return credit

    def get_taken_courses(self):
        return TakenCourse.objects.filter(student=self)

    def get_taken_credit(self):
        taken_courses = self.get_taken_courses()
        credit = 0
        for course in taken_courses:
            credit += course.credit
        return credit

    def can_edit_program(self):
        return not self.hold_state and self.reg_open_statue

    def remove_taken_course(self, ccr_course, act_course):
        taken_course = TakenCourse.objects.get(student=self, ccr_course=ccr_course, act_course=act_course)
        return taken_course.delete()

    @property
    def gpa(self):
        return self.calculate_gpa()

    @property
    def completed_credit(self):
        completed_courses = self.get_completed_courses()

        total_credit = 0
        for course in completed_courses:
            total_credit += course.credit

        return total_credit

    @property
    def standing(self):
        return standing(self.completed_credit)

    def calculate_gpa(self):
        completed_courses = self.get_completed_courses()

        total_point = 0
        total_credit = 0
        for course in completed_courses:
            total_point += (course.credit * grade_point(course.grade))
            total_credit += course.credit

        if total_point == 0:
            return 0
        return round(total_point / total_credit, 2)

    def get_maximum_credit(self):
        return maximum_credit(self.calculate_gpa())

    def __str__(self):
        return str(self.user)


class Staff(models.Model):
    # Personal Information
    user = models.OneToOneField('User', models.CASCADE)
    tc = models.CharField('TC Number', max_length=11, unique=True)
    birthday = models.DateField('Birthday')
    gender = models.CharField('Gender', max_length=10, choices=GENDER)
    joined_date = models.DateField(auto_now_add=True)

    # Contact Information
    school_email = models.EmailField('School Email', unique=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class AcademicStaff(models.Model):
    # Personal Information
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
    name = models.CharField('Institute Name', max_length=60)
    head = models.ForeignKey('AcademicStaff', models.SET_NULL, related_name='inst_head', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Name', max_length=60)
    institute = models.ForeignKey('Institute', models.CASCADE)
    dept_head = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField('Name', max_length=60)
    code = models.CharField('Code', max_length=4)
    type = models.CharField('Type', max_length=60, choices=PROGRAM_TYPES)
    thesis = models.BooleanField('Thesis', default=False)

    department = models.ForeignKey(Department, models.CASCADE)
    head = models.ForeignKey('AcademicStaff', models.SET_NULL, related_name='prog_head', blank=True, null=True)
    quota_manager = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ['code', 'type', 'thesis']
        ordering = ['type', 'name']

    def get_curriculum(self):
        return Curriculum.objects.get(program=self)

    def __str__(self):
        if self.thesis:
            return self.name + ' (With Thesis)'
        return self.name + ' (Without Thesis)'


class Curriculum(models.Model):
    program = models.ForeignKey('Program', models.CASCADE, verbose_name='Program', blank=False)
    year = models.PositiveIntegerField(verbose_name='Year', blank=False, default=datetime.now().year,
                                       validators=[MinValueValidator(2000),
                                                   MaxValueValidator(datetime.now().year + 1)])

    class Meta:
        ordering = ['program', 'year']

    def get_courses(self):
        return CcrCourse.objects.filter(ccr=self)

    def __str__(self):
        return str(self.program) + ' ' + str(self.year) + ' Curriculum'


class Course(models.Model):
    code = models.CharField('Course Code', max_length=7, unique=True)
    title = models.CharField('Course Title', max_length=60, blank=False)
    description = models.TextField('Course Description', max_length=255, blank=True)
    credit = models.IntegerField('Course Credit', blank=False)
    ects_credit = models.IntegerField('Course ECTS Credit', blank=False)
    program = models.ForeignKey('Program', models.CASCADE)
    university = models.CharField('University', max_length=60, choices=UNIVERSITIES, default='Işık Üniversitesi')
    is_valid = models.BooleanField('Is Valid', default=True)
    is_deleted = models.BooleanField('Deleted', default=False)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['program', 'code']

    def __str__(self):
        return self.code


class Section(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Course')
    number = models.PositiveIntegerField('Section Number', validators=[MinValueValidator(1)])
    quota = models.PositiveIntegerField('Quota', validators=[MinValueValidator(0)])
    instructor = models.ForeignKey('AcademicStaff', models.SET_NULL, blank=True, null=True)
    year = models.CharField('Year', max_length=4, default=datetime.now().year)
    semester = models.CharField('Semester', max_length=10, choices=SEMESTERS)

    class Meta:
        unique_together = ('course', 'number')
        ordering = ('course', 'number')

    @property
    def title(self):
        return self.course.title

    @property
    def schedules(self):
        schedule = self.get_schedule()
        days = ''
        slots = ''
        for sch in schedule:
            days += sch.day_value_short
            slots += sch.slot

        return days + ' ' + slots

    @property
    def places(self):
        schedule = self.get_schedule()
        rooms = ''
        for sch in schedule:
            rooms += (PLACES[int(sch.place)-1][1] + ' ')

        return rooms

    def get_schedule(self):
        return Schedule.objects.filter(section=self)

    def __str__(self):
        if self.number < 10:
            return self.course.code + '.0' + str(self.number)
        return self.course.code + str(self.number)

    def save(self, *args, **kwargs):
        course = getattr(self, 'course')
        year = getattr(self, 'year')
        semester = getattr(self, 'semester')
        last_section = Section.objects.filter(course=course, year=year, semester=semester)
        if last_section:
            last_no = last_section.order_by('-number').first().number
            self.number = last_no+1
        else:
            self.number = 1
        super().save(*args, **kwargs)


class Schedule(models.Model):
    section = models.ForeignKey('Section', verbose_name='Section', max_length=10, on_delete=models.CASCADE)
    day = models.CharField('Section Day', max_length=15, choices=DAYS)
    slot = models.CharField('Section Slot', max_length=2, choices=SLOTS)
    place = models.CharField('Place', max_length=15, choices=PLACES)

    class Meta:
        verbose_name = 'Course Schedule'
        unique_together = ['section', 'day', 'slot']
        ordering = ['section', 'day', 'slot']

    @property
    def day_value(self):
        return DAYS[int(self.day)-1][1]

    @property
    def day_value_short(self):
        return DAYS[int(self.day) - 1][1][0]

    @property
    def slot_value(self):
        return SLOTS[int(self.slot)-1][1]

    @property
    def place_value(self):
        return PLACES[int(self.place)-1][1]

    def __str__(self):
        return '(' + str(self.section) + ') ' \
               + self.day_value + ' ' \
               + self.slot_value + ' / ' \
               + self.place_value


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
    title = models.CharField('Title', max_length=60)
    code = models.CharField('Code', max_length=15, unique=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return str(self.code)


class CcrCourse(models.Model):
    ccr = models.ForeignKey('Curriculum', models.CASCADE)
    type = models.ForeignKey('CourseType', models.CASCADE)
    no = models.PositiveIntegerField('Course Number', validators=[MinValueValidator(1)], editable=False, default=1)
    semester = models.PositiveIntegerField('Semester', validators=[MinValueValidator(1),
                                                                   MaxValueValidator(10)])
    credit = models.PositiveIntegerField('Credit', validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ('ccr', 'type', 'no')
        ordering = ['ccr', 'type', 'no', 'semester']

    @property
    def code(self):
        offered_courses = list(self.get_offered_courses())
        if len(offered_courses) == 1:
            return offered_courses[0].act_course.code
        return str(self)

    @property
    def title(self):
        offered_courses = list(self.get_offered_courses())
        if len(offered_courses) == 1:
            return offered_courses[0].act_course.title
        return self.type.title

    def get_offered_courses(self):
        return OfferedCourse.objects.filter(ccr_course=self)

    def __eq__(self, other):
        if isinstance(other, CompletedCourse) or isinstance(other, TakenCourse):
            return self._get_pk_val() == other.ccr_course._get_pk_val()
        return isinstance(other, self.__class__) and self._get_pk_val() == other._get_pk_val()

    def __str__(self):
        return str(self.ccr.program.code) + '_' + str(self.type.code) \
               + "-" + str(write_roman(self.no))

    def save(self, *args, **kwargs):
        ccr = getattr(self, 'ccr')
        type = getattr(self, 'type')
        last_course = CcrCourse.objects.filter(ccr=ccr, type=type)
        if last_course:
            last_no = last_course.order_by('-no').first().no
            self.no = last_no + 1
        else:
            self.no = 1
        super().save(*args, **kwargs)


class OfferedCourse(models.Model):
    ccr_course = models.ForeignKey('CcrCourse', models.CASCADE)
    act_course = models.ForeignKey('Course', models.CASCADE)

    class Meta:
        unique_together = ['ccr_course', 'act_course']

    @property
    def sections(self):
        return Section.objects.filter(course=self.act_course)

    def __str__(self):
        return str(self.ccr_course.ccr.program.code) + '_' + str(self.ccr_course.type) + '-' \
               + str(write_roman(self.ccr_course.no)) + " -> " + str(self.act_course)

    def save(self, *args, **kwargs):
        if self.ccr_course.credit != self.act_course.credit:
            raise ValueError('Credit did not match')
        super().save(*args, **kwargs)


class TakenCourse(models.Model):
    student = models.ForeignKey('Student', models.CASCADE)
    ccr_course = models.ForeignKey('CcrCourse', models.CASCADE)
    act_course = models.ForeignKey('Section', models.CASCADE)

    class Meta:
        verbose_name = 'Taken Course'
        unique_together = ['student', 'ccr_course', 'act_course']

    @property
    def code(self):
        return self.act_course.course.code

    @property
    def title(self):
        return self.act_course.course.title

    @property
    def credit(self):
        return self.act_course.course.credit

    @property
    def instructor(self):
        return self.act_course.instructor

    @property
    def year(self):
        return self.act_course.year

    @property
    def semester(self):
        return self.act_course.semester

    def __eq__(self, other):
        if isinstance(other, CompletedCourse):
            return self._get_pk_val() == other.ccr_course._get_pk_val()
        if isinstance(other, CcrCourse):
            return self.ccr_course._get_pk_val() == other._get_pk_val()
        return isinstance(other, self.__class__) and self._get_pk_val() == other._get_pk_val()

    def __str__(self):
        return str(self.student) + ' ' + str(self.act_course)


class CompletedCourse(models.Model):
    student = models.ForeignKey('Student', models.CASCADE)
    ccr_course = models.ForeignKey('CcrCourse', models.CASCADE)
    act_course = models.ForeignKey('Section', models.CASCADE)
    grade = models.CharField('Grade', max_length=2, choices=GRADES)

    class Meta:
        verbose_name = 'Completed Course'
        verbose_name_plural = 'Completed Courses'
        unique_together = ['student', 'ccr_course', 'act_course']

    @property
    def year(self):
        return self.act_course.year

    @property
    def semester(self):
        return self.act_course.semester

    @property
    def credit(self):
        return self.ccr_course.credit

    def __eq__(self, other):
        if isinstance(other, TakenCourse):
            return self._get_pk_val() == other.ccr_course._get_pk_val()
        if isinstance(other, CcrCourse):
            return self.ccr_course._get_pk_val() == other._get_pk_val()
        return isinstance(other, self.__class__) and self._get_pk_val() == other._get_pk_val()

    def __str__(self):
        return str(self.student) + ' ' + str(self.ccr_course) + ' ' + str(self.grade)




#### YENi EKLENENLER ####
class ExamDate(models.Model):

    proxy = True

    place = models.CharField('Place', blank=False, null=True, max_length=6)
    date = models.DateField('Date', blank=False, null=True)
    slot = models.CharField('Slot', choices=EXAMSLOTS, null=True, blank=False, max_length=2)
    section = models.ForeignKey('Section', models.CASCADE)
    instructor = models.ForeignKey('AcademicStaff', models.CASCADE, null=True)

    class Meta: 
        verbose_name = 'Exam Date'
        verbose_name_plural = 'Exam Dates'

    def __str__(self):
        return str(self.section.course) + ' ' + str(self.section.number) + ' ' + str(self.place) + ' ' + str(self.date)

class MakeAnnouncement(models.Model):

    proxy = True

    title = models.CharField('Title', blank=False, null=True, max_length=100)
    description = models.TextField('Description', blank=False, null=True, max_length=500)
    date = models.DateField(auto_now_add=True)
    sender = models.ForeignKey('Staff', models.CASCADE, blank=False, null=True)

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return str(self.title) + ' created by ' + str(self.sender)
