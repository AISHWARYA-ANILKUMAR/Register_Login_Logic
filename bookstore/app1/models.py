from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class login(models.Model):
    
     
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    usertype=models.CharField(max_length=64)
 
    
class teacher_register(models.Model):
    
    login=models.ForeignKey('login', on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=64)
    teacher_email = models.EmailField(max_length=64, unique=True)
    teacher_phone=models.IntegerField()
    teacher_qualification=models.CharField(max_length=64)
    teacher_department=models.CharField(max_length=64)
    teacher_gender=models.CharField(max_length=64)
    
    
class student_register(models.Model):
      
    login=models.ForeignKey('login', on_delete=models.CASCADE)
    student_name=models.CharField(max_length=64)
    student_email = models.EmailField(max_length=64, unique=True)
    student_phone=models.IntegerField()
    student_course=models.CharField(max_length=64)
    student_department=models.CharField(max_length=64)
    student_gender=models.CharField(max_length=64)
