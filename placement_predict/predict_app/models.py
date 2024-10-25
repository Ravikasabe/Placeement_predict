from django.db import models


class Users(models.Model):
    sl_no = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=100,null=True, blank=True)
    ssc_p = models.FloatField(null=True, blank=True)
    ssc_b = models.CharField(max_length=100, null=True, blank=True)
    hsc_p = models.FloatField(null=True, blank=True)
    hsc_b = models.CharField(max_length=100, null=True, blank=True)
    degree_p = models.FloatField(null=True, blank=True)
    degree_t = models.CharField(max_length=100,null=True, blank=True)
    workex = models.CharField(max_length=100, null=True, blank=True)
    etest_p = models.FloatField(null=True, blank=True,default=0)
    specialisation = models.CharField(max_length=100, null=True, blank=True)
    mba_p = models.FloatField(null=True, blank=True, default=0)
    status = models.CharField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=False,null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    ssc_y = models.IntegerField(null=True, blank=True)
    hsc_y = models.IntegerField(null=True, blank=True)
    degree = models.CharField(max_length=200,null=True, blank=True)
    university = models.CharField(max_length=200, null=True, blank=True)
    Stream = models.CharField(max_length=200, null=False)
    degree_passoutYear = models.CharField(max_length=200,null=True, blank=True)
    workex_company = models.CharField(max_length=200, null=True, blank=True)
    skills = models.CharField(max_length=500, null=True, blank=True)
    certificates = models.CharField(max_length=500, null=True, blank=True)
    resume = models.FileField(null=True, blank=True)


    
