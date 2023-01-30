from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=100)

class Reg_stud(models.Model):
    login_id=models.OneToOneField(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    gender=models.CharField(max_length=100)
    cource=models.CharField(max_length=100)
    date_joining=models.DateField(max_length=100,unique=True)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=30)

class Reg_teach(models.Model):
    login_id=models.OneToOneField(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    gender=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    date_joining=models.DateField(max_length=100,unique=True)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=30)

class Apply_leave(models.Model):
    start_date=models.DateField(max_length=100,unique=True)
    end_date=models.DateField(max_length=100,unique=True)
    reason=models.CharField(max_length=100)

class teach_leave(models.Model):
    start_date=models.DateField(max_length=100,unique=True)
    end_date=models.DateField(max_length=100,unique=True)
    reason=models.CharField(max_length=100)

# class Attendence(models.Model):
#     stud_name=models.CharField(max_length=100)
#     teach_name=models.CharField(max_length=100)
#     cource=models.CharField(max_length=100)
#     date=models.DateField(max_length=100,unique=True)

class Exam(models.Model):
    name=models.CharField(max_length=100)
    subject1=models.IntegerField()
    subject2=models.IntegerField()
    subject3=models.IntegerField()
    subject4=models.IntegerField()


    