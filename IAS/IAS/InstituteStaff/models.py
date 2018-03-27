from django.db import models

sex = (('erkek', 'ERKEK'), ('kadın', 'KADIN'))

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
    city = models.CharField(('Current city'), max_length=20, blank=False, default='null')
    phoneNumber = models.CharField(('Phone Number'), max_length=11, blank=False, default='null', unique=True)

    # İş bilgileri:
    #startingDate = models.DateTimeField(('Starting Date'), default='2018-03-23')
    ssn = models.CharField(('SSN'), max_length=11, default='null', blank=False, unique=True)
    #staffID = models.CharField(('ID'), max_length=10, )

class PushNotification(models.Model):
    senderID = models.CharField(('Sender ID'), max_length=10, default='null', blank=False)
    text = models.TextField(('Text'), max_length=500, default='null')
