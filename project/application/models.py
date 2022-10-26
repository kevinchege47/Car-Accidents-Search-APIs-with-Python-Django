from django.db import models


class Accidents(models.Model):
    LEVELS = (
        ('Fatal Injury Crash','Fatal Injury Crash'),
        ('Major Injury Crash','Major Injury Crash'),
        ('Minor Injury Crash','Minor Injury Crash'),
        ('Minimal Injury Crash','Minimal Injury Crash'),
    
    )
    cause = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    degreeseverity = models.CharField(max_length=50,null=True,choices=LEVELS)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __string__(self):
        return self.location

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=50,null=True)
    head_office_location = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=15,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __string__(self):
        return self.name
class Cars(models.Model):

    numberplate = models.CharField(max_length=50,unique=True,null=True)
    makemodel = models.CharField(max_length=50,null=True)
    driverphone = models.CharField(max_length=15,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    accidents = models.ManyToManyField(Accidents,blank=True)
    # insurancecompany = models.ManyToManyField(InsuranceCompany)

    def __str__(self):
        return self.numberplate
# Create your models here.
