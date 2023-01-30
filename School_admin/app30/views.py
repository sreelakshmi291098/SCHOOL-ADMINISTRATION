from django.shortcuts import render,redirect
from app30.models import Reg_stud,login,Reg_teach,Apply_leave,teach_leave,Exam
from django.contrib.auth.views import auth_login
from . import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if login.objects.filter(username = username, password=password ).exists(): 
            data = login.objects.filter(username = username, password=password ).values() 
            for i in data:
                id = i['id']
                role = i['role']
                user_name=i['username']
                print(id)
                print(user_name)    
            if Reg_stud.objects.filter(login_id_id=id).exists():
                
                da = Reg_stud.objects.filter(login_id_id = id).values()
                for i in da:
                    status = i['status']
                    print(status) 
                
                    if da is not None and role == 'student' and status == '1':
                        return redirect('student')
                return HttpResponse('heloo')    
            elif Reg_teach.objects.filter(login_id_id = id).exists():
                fa = Reg_teach.objects.filter(login_id_id = id).values()
                for i in fa:
                    status = i['status']

                    if fa is not None and role == 'teacher' and status == '1':
                        return redirect('teacher')    
            elif username == 'sreelakshmi' and password == 'sree123':
                return redirect('adminpage')
    else:
        context= {}
        return render(request, 'login.html', context)

def admin(request):
    return render(request,'admin.html')

def student(request):
    return render(request,'student.html')

def teacher(request):
    return render(request,'teacher.html')

def hod(request):
    return render(request,'hod.html')

def stud_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('conformpassword')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phonenumber=request.POST.get('number')
        gender=request.POST.get('gender')
        cource=request.POST.get('cource')
        date_joining=request.POST.get('date')
        status="0"
        role="student"
        
        user=models.login(username=username,password=password1,role=role)
        user.save()
        print (user.id)
        log_id=user.id
        
        userDetail=models.Reg_stud(login_id_id=log_id,name=name,email=email,address=address,phone_number=phonenumber,gender=gender,cource=cource,date_joining=date_joining,status=status,role=role)
        userDetail.save()

        print('user created')
        
        return redirect("loginpage")
    else:
        return render(request,'stud_reg.html')

def teach_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('conformpassword')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phonenumber=request.POST.get('number')
        gender=request.POST.get('gender')
        subject=request.POST.get('subject')
        date_joining=request.POST.get('date')
        status="0"
        role="teacher"
        
        user=models.login(username=username,password=password1,role=role)
        user.save()
        log_id=user.id

        userDetail=models.Reg_teach(login_id_id=log_id,name=name,email=email,address=address,phone_number=phonenumber,gender=gender,subject=subject,date_joining=date_joining,status=status,role=role)
        userDetail.save()

        print('user created')
        
        return redirect("loginpage")
    else:
        return render(request,'teach_reg.html')

def stud_leave(request):
    if request.method=='POST':
        startdate=request.POST.get('start')
        enddate=request.POST.get('end')
        reason=request.POST.get('reason')

        userDetail=models.Apply_leave(start_date=startdate,end_date=enddate,reason=reason)
        userDetail.save()
        return redirect("adminpage")
    return render(request,'stud_leave.html')

def teacher_leave(request):
    if request.method=='POST':
        startdate=request.POST.get('start')
        enddate=request.POST.get('end')
        reason=request.POST.get('reason')

        userDetail=models.teach_leave(start_date=startdate,end_date=enddate,reason=reason)
        userDetail.save()
        return redirect("adminpage")
    return render(request,'teach_leave.html')

def exam(request):
    if request.method=='POST':
        name=request.POST.get('name')
        subject1=request.POST.get('subject1')
        subject2=request.POST.get('subject2')
        subject3=request.POST.get('subject3')
        subject4=request.POST.get('subject4')


        userDetail=models.Exam(name=name,subject1=subject1,subject2=subject2,subject3=subject3,subject4=subject4)
        userDetail.save()
        return redirect("adminpage")
    return render(request,'exam.html')

def science(request):
    return render(request,'science.html')

def humanities(request):
    return render(request,'humanities.html')

def commerce(request):
    return render(request,'commerce.html')

def science_first(request):
    return render(request,'science_first.html')

def science_second(request):
    return render(request,'science_second.html')

def human_first(request):
    return render(request,'human_first.html')

def human_second(request):
    return render(request,'human_second.html')

def commerce_first(request):
    return render(request,'commerce_first.html')

def commerce_second(request):
    return render(request,'commerce_second.html')

def attendence(request):
    return render(request,'student_attendence.html')

def student_pending(request):
    data=Reg_stud.objects.all()
    return render(request,'viewstudentpending.html',{'data':data})

def teacher_pending(request):
    data=Reg_teach.objects.all()
    return render(request,'viewteacherpending.html',{'data':data})

def student_approve(request,reg_id):
    reg=Reg_stud.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("student_pending")

def student_reject(request,reg_id):
    item=Reg_user.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("student_pending")

def teacher_approve(request,reg_id):
    reg=Reg_teach.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("teacher_pending")

def teacher_reject(request,reg_id):
    item=Reg_teach.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("teacher_pending")

def approvedstud(request):
    data=Reg_stud.objects.all()
    return render(request,'approvedstud.html',{'data':data})

def approvedteach(request):
    data=Reg_teach.objects.all()
    return render(request,'approvedteach.html',{'data':data})

def stud_delete(request,reg_id):
    add=Reg_stud.objects.get(id=reg_id)
    add.delete()
    return redirect('approvedstud')

def teach_delete(request,reg_id):
    dele=Reg_teach.objects.get(id=reg_id)
    dele.delete()
    return redirect('approvedteach')

def viewstudleave(request):
    data=Apply_leave.objects.all()
    return render(request,'viewstudleave.html',{'data':data})

def viewteachleave(request):
    data=teach_leave.objects.all()
    return render(request,'viewteachleave.html',{'data':data})
