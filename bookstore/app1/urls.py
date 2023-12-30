
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('all_login',views.all_login),
    path('admin_page',views.admin_page),
    path('student_page',views.student_page),
    path('teacher_page',views.teacher_page),
    path('register_teacher',views.register_teacher),
    path('register_student',views.register_student),
   
    

]
