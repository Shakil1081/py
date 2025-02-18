from django.db import models

# Create your models here.
class Reagostation(models.Model):
    FullName = models.CharField(max_length=50)
    EmailAddress = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=14)
    Gender = models.CharField(max_length=30)
    DateofBirth = models.CharField(max_length=22)
    Course = models.CharField(max_length=100)
    Address = models.CharField(max_length=30)
    Agree = models.CharField(max_length=1)

    def __str__(self):
        return self.FullName + ' '+ self.PhoneNumber+' '+ self.Address
