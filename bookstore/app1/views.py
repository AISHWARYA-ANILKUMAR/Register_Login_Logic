from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    
    
    return render(request,'index.html')

def admin_page(request):
    
    return render(request,'admin_page.html')


def teacher_page(request):
    
    return render(request,'teacher_page.html')

def student_page(request):
    
    
    return render(request,'student_page.html')

def all_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']

        try:
            q = login.objects.get(username=uname, password=passwd)

            if q:
                if q.usertype == 'admin':
                    return HttpResponse("<script>alert('login successful');window.location='admin_page'</script>")
                elif q.usertype == 'student':
                    return HttpResponse("<script>alert('login successful');window.location='student_page'</script>")
                elif q.usertype == 'teacher':
                    return HttpResponse("<script>alert('login successful');window.location='teacher_page'</script>")
            else:
                return HttpResponse("<script>alert('invalid login credentials');window.location='all_login'</script>")
        except login.DoesNotExist:
            return HttpResponse("<script>alert('Invalid login credentials');window.location='all_login'</script>")

    return render(request, 'all_login.html')



def register_teacher(request):
     
     if request.method == 'POST':
         
         
        name=request.POST['teacher_name']
        email=request.POST['teacher_email']
        phone=request.POST['teacher_phone']
        qualification=request.POST['teacher_qualification']
        department=request.POST['teacher_department']
        gender=request.POST['teacher_gender']
        uname=request.POST['teacher_username']
        passwd=request.POST['teacher_password']
    
    
        qry=login.objects.filter(username=uname)
    
        if qry:
            
        
            return HttpResponse("<script> alert('user already exits');windows.loaction='/register_teacher'</script>")
        else:
            
            q=login(username=uname,password=passwd,usertype='teacher')
            q.save()
            obj=teacher_register(login=q,teacher_name=name,teacher_email=email,teacher_phone=phone,teacher_qualification=qualification,teacher_department=department,teacher_gender=gender)
            obj.save()
            
     return render(request, 'register_teacher.html')
            
def register_student(request):
    
    if request.method == 'POST':
        

        stu_name=request.POST['stud_name']
        stu_email=request.POST['stud_email']
        stu_phone=request.POST['stud_phone']
        stu_course=request.POST['stud_course']
        stu_dept=request.POST['stud_dept']
        stu_gender=request.POST['stud_gender']
        uname=request.POST['username']
        passwd=request.POST['password']
        
        qry=login.objects.filter(username=uname)
        
        if qry:
            return HttpResponse("<script> alert('user already exits');windows.location='/register_student'</script>")
        else:
            q=login(username=uname,password=passwd,usertype='student')
            q.save()
            obj=student_register(login=q,student_name=stu_name,student_phone=stu_phone,student_email=stu_email,student_course=stu_course,student_department=stu_dept,student_gender=stu_gender)
            obj.save()
            
    return render(request, 'register_student.html')
    
        
        