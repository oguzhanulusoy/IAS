from django.db import models
from django.core.validators import MaxValueValidator


# mezuniyet dereceleri:
listOfDegree = (('1', 'Lisans'),
                ('2', 'Yüksek Lisans'),
                ('3', 'Doktora'))

# şehir listesi:

listOfCities = (('1','Adana'),
('2','Adıyaman'),
('3','Afyonkarahisar'),
('4','Ağrı'),
('5','Amasya'),
('6','Ankara'),
('7','Antalya'),
('8','Artvin'),
('9','Aydın'),
('10','Balıkesir'),
('11','Bilecik'),
('12','Bingöl'),
('13','Bingöl'),
('14','Bolu'),
('15','Burdur'),
('16','Bursa'),
('17','Çanakkale'),
('18','Çankırı'),
('19','Çorum'),
('20','Denizli'),
('21','Diyarbakır'),
('22','Edirne'),
('23','Elazığ'),
('24','Erzincan'),
('25','Erzurum'),
('26','Eskişehir'),
('27','Gaziantep'),
('28','Giresun'),
('29','Gümüşhane'),
('30','Hakkâri'),
('31','Hatay'),
('32','Isparta'),
('33','Mersin'),
('34','İstanbul'),
('35','İzmir'),
('36','Kars'),
('37','Kastamonu'),
('38','Kayseri'),
('39','Kırklareli'),
('40','Kırşehir'),
('41','Kocaeli'),
('42','Konya'),
('43','Kütahya'),
('44','Malatya'),
('45','Manisa'),
('46','Kahramanmaraş'),
('47','Mardin'),
('48','Muğla'),
('49','Muş'),
('50','Nevşehir'),
('51','Niğde'),
('52','Ordu'),
('53','Rize'),
('54','Sakarya'),
('55','Samsun'),
('56','Siirt'),
('57','Sinop'),
('58','Sivas'),
('59','Tekirdağ'),
('60','Tokat'),
('61','Trabzon'),
('62','Tunceli'),
('63','Şanlıurfa'),
('64','Uşak'),
('65','Van'),
('66','Yozgat'),
('67','Zonguldak'),
('68','Aksaray'),
('69','Bayburt'),
('70','Karaman'),
('71','Kırıkkale'),
('72','Batman'),
('73','Şırnak'),
('74','Bartın'),
('75','Ardahan'),
('76','Iğdır'),
('77','Yalova'),
('78','Karabük'),
('79','Kilis'),
('80','Osmaniye'),
('81','Düzce'))

# okul listesi:
listOfUniversities = (
('1','Işık Üniversitesi'),
('2','Abant İzzet Baysal Üniversitesi'),
('3','Adana Bilim ve Teknoloji Üniversitesi'),
('4','Adıyaman Üniversitesi'),
('5','Adnan Menderes Üniversitesi'),
('6','Afyon Kocatepe Üniversitesi'),
('7','Ağrı İbrahim Çeçen Üniversitesi'),
('8','Ahi Evran Üniversitesi'),
('9','Akdeniz Üniversitesi'),
('10','Aksaray Üniversitesi'),
('11','Alanya Alaaddin Keykubat Üniversitesi'),
('12','Amasya Üniversitesi'),
('13','Anadolu Üniversitesi'),
('14','Ankara Üniversitesi'),
('15','Ankara Sosyal Bilimler Üniversitesi'),
('16','Ardahan Üniversitesi'),
('17','Artvin Çoruh Üniversitesi'),
('18','Atatürk Üniversitesi'),
('19','Balıkesir Üniversitesi'),
('20','Bandırma Onyedi Eylül Üniversitesi'),
('21','Bartın Üniversitesi'),
('22','Batman Üniversitesi'),
('23','Bayburt Üniversitesi'),
('24','Bilecik Şeyh Edebali Üniversitesi'),
('25','Bingöl Üniversitesi'),
('26','Bitlis Eren Üniversitesi'),
('27','Boğaziçi Üniversitesi'),
('28','Bozok Üniversitesi'),
('29','Bursa Teknik Üniversitesi'),
('30','Celal Bayar Üniversitesi'),
('31','Cumhuriyet Üniversitesi'),
('32','Çanakkale Onsekiz Mart Üniversitesi'),
('33','Çankırı Karatekin Üniversitesi'),
('34','Çukurova Üniversitesi'),
('35','Deniz Harp Okulu'),
('36','Dicle Üniversitesi'),
('37','Dokuz Eylül Üniversitesi'),
('38','Dumlupınar Üniversitesi'),
('39','Düzce Üniversitesi'),
('40','Ege Üniversitesi'),
('41','Erciyes Üniversitesi'),
('42','Erzincan Üniversitesi'),
('43','Erzurum Teknik Üniversitesi'),
('44','Eskişehir Osmangazi Üniversitesi'),
('45','Fırat Üniversitesi'),
('46','Galatasaray Üniversitesi'),
('47','Gazi Üniversitesi'),
('48','Gaziantep Üniversitesi'),
('49','Gaziosmanpaşa Üniversitesi'),
('50','Gebze Teknik Üniversitesi'),
('51','Giresun Üniversitesi'),
('52','Gümüşhane Üniversitesi'),
('53','Hacettepe Üniversitesi'),
('54','Hakkari Üniversitesi'),
('55','Harran Üniversitesi'),
('56','Hava Harp Okulu'),
('57','Hitit Üniversitesi'),
('58','Iğdır Üniversitesi'),
('59','İnönü Üniversitesi'),
('60','İskenderun Teknik Üniversitesi'),
('61','İstanbul Medeniyet Üniversitesi'),
('62','İstanbul Üniversitesi'),
('63','İstanbul Teknik Üniversitesi'),
('64','İzmir Bakırçay Üniversitesi'),
('65','İzmir Demokrasi Üniversitesi'),
('66','İzmir Kâtip Çelebi Üniversitesi'),
('67','İzmir Yüksek Teknoloji Enstitüsü'),
('68','Kafkas Üniversitesi'),
('69','Kahramanmaraş Sütçü İmam Üniversitesi'),
('70','Karabük Üniversitesi'),
('71','Karadeniz Teknik Üniversitesi'),
('72','Karamanoğlu Mehmetbey Üniversitesi'),
('73','Kastamonu Üniversitesi'),
('74','Kırıkkale Üniversitesi'),
('75','Kilis 7 Aralık Üniversitesi'),
('76','Kocaeli Üniversitesi'),
('78','Necmettin Erbakan Üniversitesi'),
('79','Mardin Artuklu Üniversitesi'),
('80','Marmara Üniversitesi'),
('81','Mehmet Akif Ersoy Üniversitesi'),
('82','Mersin Üniversitesi'),
('83','Mimar Sinan Güzel Sanatlar Üniversitesi'),
('84','Muğla Sıtkı Koçman Üniversitesi'),
('85','Mustafa Kemal Üniversitesi'),
('86','Muş Alparslan Üniversitesi'),
('87','Namık Kemal Üniversitesi'),
('88','Nevşehir Hacı Bektaş Veli Üniversitesi'),
('89','Niğde Üniversitesi'),
('90','Ondokuz Mayıs Üniversitesi'),
('91','Ordu Üniversitesi'),
('92','Orta Doğu Teknik Üniversitesi'),
('93','Osmaniye Korkut Ata Üniversitesi'),
('94','Pamukkale Üniversitesi'),
('95','Sakarya Üniversitesi'),
('96','Selçuk Üniversitesi'),
('97','Siirt Üniversitesi'),
('98','Süleyman Demirel Üniversitesi'),
('99','Trakya Üniversitesi'),
('100','Uludağ Üniversitesi'),
('101','Uşak Üniversitesi'),
('102','Yalova Üniversitesi'),
('103','Yıldız Teknik Üniversitesi'),
('104','Yıldırım Beyazıt Üniversitesi'),
('105','Yüzüncü Yıl Üniversitesi'),
('106','Bülent Ecevit Üniversitesi'),
('107','Acıbadem Üniversitesi'),
('108','Akev Üniversitesi'),
('109','Anka Teknoloji Üniversitesi'),
('110','Atılım Üniversitesi'),
('111','Avrasya Üniversitesi'),
('112','Bahçeşehir Üniversitesi'),
('113','Başkent Üniversitesi'),
('114','Beykent Üniversitesi'),
('115','Bezmiâlem Vakıf Üniversitesi'),
('116','Bilkent Üniversitesi'),
('117','Biruni Üniversitesi'),
('118','Çankaya Üniversitesi'),
('119','Çağ Üniversitesi'),
('120','Doğuş Üniversitesi'),
('121','Fatih Sultan Mehmet Üniversitesi'),
('122','Haliç Üniversitesi'),
('123','İstanbul 29 Mayıs Üniversitesi'),
('124','İstanbul Arel Üniversitesi'),
('125','İstanbul Aydın Üniversitesi'),
('126','İstanbul Bilgi Üniversitesi'),
('127','İstanbul Gelişim Üniversitesi'),
('128','İstanbul Kemerburgaz Üniversitesi'),
('129','İstanbul Kültür Üniversitesi'),
('130','İstanbul Medipol Üniversitesi'),
('131','İstanbul Şehir Üniversitesi'),
('132','İstinye Üniversitesi'),
('132','İzmir Ekonomi Üniversitesi'),
('133','Kadir Has Üniversitesi'),
('134','Nişantaşı Üniversitesi'),
('135','Okan Üniversitesi'),
('136','Özyeğin Üniversitesi'),
('137','Piri Reis Üniversitesi'),
('138','Sabancı Üniversitesi'),
('139','TED Üniversitesi'),
('140','Yeditepe Üniversitesi'))

# program listesi:
listOfPrograms = (('cse', 'CSE'), ('se', 'SE'))
# programlar fk dan gelecek ardından

# cinsiyet listesi:
sex = (('1', 'Female'), ('2', 'Man'))

listOfSemesters = (('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer'))
listOfYears = (('2018', '2018'),('2019','2019'),('2020','2020'),('2021', '2021'), ('2022','2022'))
listOfDays = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'))
listOfTimeIntervals = (('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'))
listOfMilitaryStatues = (('1', 'Yes'), ('2', 'No'))

class BuildingSchema(models.Model):

    class Meta:
        verbose_name_plural = "Building Schema"

    name = models.CharField(('Class No'), null=True, blank=False, unique=True, max_length=3)

    def __str__(self):
        return str(self.name)

class Classes(models.Model):

    class Meta:

        verbose_name_plural = "Classes"

    className = models.ForeignKey(BuildingSchema, on_delete=models.CASCADE, null=True, blank=False)
    days = models.CharField(('Date'), choices=listOfDays, null=True, blank=False, max_length=10)
    timeIntervals = models.CharField(('Time Intervals'), choices=listOfTimeIntervals, null=True, blank=False, max_length=3)

    def __str__(self):
        return str(str(self.className)+" "+str(self.days)+" "+str(self.timeIntervals))

class Semester(models.Model):

    class Meta:
        verbose_name_plural = "Semesters"

    year = models.IntegerField(('Year'), default=2018, blank=False, max_length=4)
    period = models.CharField(('Period'), choices=listOfSemesters, blank=False, max_length=6, null=True)

    def __str__(self):
        return str(str(self.year)+" "+str(self.period))

class InstituteStaff(models.Model):

    class Meta:
        verbose_name_plural = "Institute Staffs"

    # Kimlik bilgileri:
    firstName = models.CharField(('First Name'), max_length=15, blank=False)
    middleName = models.CharField(('Middle Name'), max_length=15, blank=True)
    lastName = models.CharField(('Last Name'), max_length=15, blank=False)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcNumber = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), default='Kadın', max_length=5, choices=sex)

    # İletişim bilgileri:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, blank=False, choices=listOfCities, default='İstanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='Phone Number', unique=True)

    # İş bilgileri:
    #startingDate = models.DateTimeField(('Starting Date'), null=True)
    ssn = models.CharField(('SSN'), max_length=11, default='SSN', blank=False, unique=True)
    #staffID = models.CharField(('ID'), max_length=10, null=True) özel bir ID olacaksa eğer, ig. 214CS2015

    def __str__(self):
        return str(self.firstName+" "+self.lastName)

class Apply(models.Model):

    class Meta:
        verbose_name_plural = "Applies"

    # Kimlik bilgileri:
    firstName = models.CharField(('First Name'), max_length=15, blank=False)
    middleName = models.CharField(('Middle Name'), max_length=15, blank=True)
    lastName = models.CharField(('Last Name'), max_length=15, blank=False)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcNumber = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), max_length=5, choices=sex, default='Female')

    # İletişim bilgileri:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, choices=listOfCities, blank=False, default='İstanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='00000000000', unique=True)

    # Başvuru bilgileri:
    degree = models.CharField(('Degree'), max_length=20, choices=listOfDegree, default='Lisans')
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, default='Işık Üniversitesi')
    gpa = models.PositiveSmallIntegerField(('General Point Average'), blank=False, validators=[MaxValueValidator(4)])
    scienceExam = models.PositiveSmallIntegerField(('ALES Point'), blank=False, validators=[MaxValueValidator(100)])
    foreignLanguageExam = models.PositiveSmallIntegerField(('YDS Point'), blank=False, validators=[MaxValueValidator(100)])
    program = models.CharField(('Program'), max_length=40, choices=listOfPrograms, default='cse')

    def __str__(self):
        return self.tcNumber

class AcademicInstructor(models.Model):

    class Meta:
        verbose_name_plural = "Academic Instructors"

# Kimlik bilgileri:
    firstName = models.CharField(('First Name'), max_length=15, blank=False)
    middleName = models.CharField(('Middle Name'), max_length=15, blank=True)
    lastName = models.CharField(('Last Name'), max_length=15, blank=False)
    joinedDate = models.DateTimeField(auto_now_add=True)
    tcNumber = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), default='Kadın', max_length=5, choices=sex)

    # İletişim bilgileri:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False)
    city = models.CharField(('Current city'), max_length=20, choices=listOfCities, blank=False, default='İstanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='Phone Number', unique=True)

    # İş bilgileri:
    startingDate = models.DateTimeField(('Starting Date'), null=True)
    ssn = models.CharField(('SSN'), max_length=11, default='SSN', blank=False, unique=True)
    #staffID = models.CharField(('ID'), max_length=10, )


    def __str__(self):
        return self.firstName+" "+self.lastName

class Instructor(models.Model):

    class Meta:
        verbose_name_plural = "Instructor List"

    name = models.ForeignKey(AcademicInstructor, on_delete=models.CASCADE, null=True, blank=False, related_name="fullname", unique=True)

    def __str__(self):
        return str(self.name)

class Head(models.Model):

    class Meta:
        verbose_name_plural = "Head of Departments"

    name = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False, related_name="firstName", unique=True)

    def __str__(self):
        return str(self.name)

class Department(models.Model):

    class Meta:
        verbose_name_plural = "Departments"

    code = models.CharField(('Code'), blank=False, default='Code', max_length=3, unique=True)
    definition = models.CharField(('Definition'), blank=False, default='Definition', max_length=50)
    head = models.ForeignKey(Head, on_delete=models.CASCADE, null=True, blank=False, related_name='head', unique=True)

    def __str__(self):
        return str(self.code+" "+self.definition)

class Program(models.Model):

    class Meta:
        verbose_name_plural = "Programs"

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=False, related_name='department')
    name = models.CharField(('Name'), blank=False, default='Name', max_length=50, unique=True)

    def __str__(self):
        return str(self.name)

class Course(models.Model):

    class Meta:
        verbose_name_plural = "Courses"

    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=False, related_name='program1')
    code = models.CharField(('Code'), blank=False, default='Code', max_length=3, unique=True)
    definition = models.CharField(('Definition'), blank=False, default='Definition', max_length=50)
    date = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=False, related_name='date')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False, related_name='instructor')
    credit = models.PositiveSmallIntegerField(('Credit'), blank=False, null=True, default=3)

    def __str__(self):
        return str(self.code)

class TakenCourse(models.Model):

    class Meta:
        verbose_name_plural = "Taken Courses"

    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=False, related_name='program2')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=False, related_name='course')

    def __str__(self):
        return self.course.definition

class RequestOpenCourse(models.Model):

    class Meta:
        verbose_name_plural ="Requests to Course"

    instructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False, related_name='RequestOpenCourse.instructorID+')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=False, related_name='RequestOpenCourse.program+')
    course = models.ForeignKey(TakenCourse, on_delete=models.CASCADE, null=True, blank=False, related_name='RequestOpenCourse.course+')
    day = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=False, related_name='RequestOpenCourse.day+')
    approval = models.CharField(('Approval'), blank=True, null=True, max_length=1, default='0')

    def __str__(self):
        return str(str(self.program)+" "+str(self.course)+" "+str(self.day))

class OpenCourse(models.Model):

    class Meta:
        verbose_name_plural = "Open Courses"

    program = models.ForeignKey(RequestOpenCourse, on_delete=models.CASCADE, null=True, blank=False, related_name='program3')
    course = models.ForeignKey(RequestOpenCourse, on_delete=models.CASCADE, null=True, blank=False, related_name='course2')
    placeAndDate = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=False, related_name='classes+')
    approval = models.ForeignKey(RequestOpenCourse, on_delete=models.CASCADE, null=True, blank=False, related_name='OpenCourse.approval+')

    def __str__(self):
        return str(str(self.course)+" "+str(self.placeAndDate))

class Form(models.Model):

    class Meta:
        verbose_name_plural = "Forms"

    formID = models.PositiveSmallIntegerField(('Form ID'), unique=True, null=True, blank=False)
    title = models.CharField(('Title'), max_length=200, unique=True, null=True, blank=False)
    description = models.CharField(('Descriptipn'), max_length=500, null=True, blank=False)
    link = models.URLField(verbose_name='Link',name='helloo',unique=True)

    def __str__(self):
        return self.title

class Report(models.Model):

    class Meta:
        verbose_name_plural = "Reports"

    reportID = models.PositiveSmallIntegerField(('Report ID'), unique=True, null=False, blank=False, auto_created=True, primary_key=True)
    title = models.CharField(('Title'), max_length=200, unique=True, null=True, blank=False)
    content = models.CharField(('Content'), max_length=2000, null=True, blank=False)
    link = models.CharField(('Link (if exists)'), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class GrandStudent(models.Model):

    class Meta:
        verbose_name_plural = "Grand Students"

    # Kimlik bilgileri:
    firstName = models.CharField(('First Name'), max_length=15, blank=False, null=True)
    middleName = models.CharField(('Middle Name'), max_length=15, blank=True, null=True)
    lastName = models.CharField(('Last Name'), max_length=15, blank=False, null=True)
    joinedDate = models.DateTimeField(auto_now_add=True,null=True)
    tcNumber = models.CharField(('TC Number'), max_length=11, blank=False, unique=True)
    birthday = models.DateField(('Birthday'), null=True, blank=False)
    gender = models.CharField(('Sex'), default='Kadın', max_length=5, choices=sex)
    militaryStatue = models.CharField(('Military Statue'), choices=listOfMilitaryStatues, max_length=3, default='No', blank=True)

    # İletişim bilgileri:
    mail = models.EmailField(('E-mail Address'), unique=True)
    address = models.CharField(('Address'), max_length=40, blank=False, null=True)
    city = models.CharField(('Current city'), max_length=20, blank=False, choices=listOfCities, default='İstanbul')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='00000000000', unique=True)

    # Başvuru bilgileri:
    degree = models.CharField(('Degree'), max_length=20, choices=listOfDegree, default='Lisans')
    university = models.CharField(('University'), max_length=50, choices=listOfUniversities, default='Işık Üniversitesi')
    gpa = models.PositiveSmallIntegerField(('General Point Average'), blank=False, validators=[MaxValueValidator(4)], null=True)
    scienceExam = models.PositiveSmallIntegerField(('ALES Point'), blank=False, validators=[MaxValueValidator(100)], null=True)
    foreignLanguageExam = models.PositiveSmallIntegerField(('YDS Point'), blank=False, validators=[MaxValueValidator(100)], null=True)
    transcript = models.URLField(verbose_name='Transcript Link', blank=False, unique=True, null=True)

    # Enstitü bilgileri:
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=False, related_name='program4')
    academicSupervisior = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False, related_name='academicSupervisior')
    semester = models.PositiveSmallIntegerField(('Statue'), blank=False, validators=[MaxValueValidator(4)], default=1)
    scholarship = models.PositiveSmallIntegerField(('Scholarship'), validators=[MaxValueValidator(100)])
    studentID = models.CharField(('Student ID'), max_length=9, unique=True)
    startingDate = models.DateField(('Starting Date'), default='2018-03-23')
    endingDate = models.DateField(('Ending Date'), default='2018-03-23')
    gpaI = models.PositiveSmallIntegerField(('GPA'), validators=[MaxValueValidator(4)], default='0')
    completedCredit = models.CharField(('Completed Credit'), default='0', max_length=3)

    def __str__(self):
        return str(self.studentID+" "+self.firstName+" "+self.lastName)

class Supervisior(models.Model):

    class Meta:

        verbose_name_plural = "Supervisiors"

    academicInstructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False, related_name='academicInstructor')
    grandS = models.ForeignKey(GrandStudent, on_delete=models.CASCADE, null=True, blank=False, related_name='grandS', unique=True)

    def __str__(self):
        return str(self.academicInstructor)

class WeeklyScheduleI(models.Model):

    class Meta:
        verbose_name_plural = "Weekly Schedules for Instructors"

    instructorID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=False, related_name='instructorID')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=False, related_name='courseID')

    def __str__(self):
        return str(str(self.instructorID)+" "+str(self.course))

class WeeklyScheduleS(models.Model):

    class Meta:
        verbose_name_plural = "Weekly Schedules for Students"

    studentID = models.ForeignKey(GrandStudent, on_delete=models.CASCADE, null=True, blank=False, related_name='IDofStudent' )
    course = models.ForeignKey(OpenCourse, on_delete=models.CASCADE, null=True, blank=False, related_name='NameOfCourse')

    def __str__(self):
        return str(str(self.studentID)+" "+str(self.course))

class PushNotificationIStoInstructors(models.Model):

    class Meta:
        verbose_name_plural = "Push Notifications from Institute to Instructors"

    institute = models.ForeignKey(InstituteStaff, on_delete=models.CASCADE, null=True, blank=False, related_name='sender2instructors')
    instructors = models.ManyToManyField(Instructor, null=True, blank=False, related_name='receiverFromInstitute')
    subject = models.CharField(('Subject'), max_length=140, null=True, blank=False)
    text = models.TextField(('Text'), max_length=500, null=True, blank=False)

    def __str__(self):
        return str(str(self.institute)+" "+str(self.subject))

class PushNotificationIStoStudents(models.Model):

    class Meta:
        verbose_name_plural = "Push Notifications from Institute to Students"

    institute = models.ForeignKey(InstituteStaff, on_delete=models.CASCADE, null=True, blank=False, related_name='sender2tostudents2')
    grandStudents = models.ManyToManyField(GrandStudent, null=True, blank=False, related_name='receiverFromInstitute2')
    subject = models.CharField(('Subject'), max_length=140, null=True, blank=False)
    text = models.TextField(('Text'), max_length=500, null=True, blank=False)

    def __str__(self):
        return str(str(self.institute)+" "+str(self.subject))

class PushNotificationAItoStudents(models.Model):

    class Meta:
        verbose_name_plural = "Push Notifications from Academic Instructors to Students"

    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=False, related_name='sender2students')
    grandStudents = models.ManyToManyField(GrandStudent, null=True, blank=False, related_name='receiverFromInstructors')
    subject = models.CharField(('Subject'), max_length=140, null=True, blank=False)
    text = models.TextField(('Text'), max_length=500, null=True, blank=False)

    def __str__(self):
        return str(str(self.instructor)+" "+str(self.subject))

class Question(models.Model):

    class Meta:
        verbose_name_plural = "Questions"

    questionText = models.CharField(('Question Text'), max_length=140, null=True, blank=False)
    publishedDate = models.DateTimeField('Published Date')

    def __str__(self):
        return self.questionText

class Choice(models.Model):

    class Meta:
        verbose_name_plural = "Choices for Questions"

    choiceText = models.CharField(('Choice Text'), max_length=140, null=True, blank=False)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.choiceText

class CCR(models.Model):

    class Meta:
        verbose_name_plural = "CCRs"

    studentID = models.ForeignKey(GrandStudent, on_delete=models.CASCADE, null=True, blank=False, related_name='GrandStudent.studentID+')
    program = models.ForeignKey(GrandStudent, on_delete=models.CASCADE, null=True, blank=False, related_name='GrandStudent.program+')
    takenCourses = models.ForeignKey(TakenCourse, on_delete=models.CASCADE, null=True, blank=False, related_name='CCR.takenCourses+')
    #completedLectures

    def __str__(self):
        return str(str(self.studentID)+" "+str(self.program)+" "+str(self.takenCourses))





# completed course lar

