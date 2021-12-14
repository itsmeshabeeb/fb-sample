from django.http import response
from django.shortcuts import redirect, render
from . models import *

# Create your views here.


def fun1(request):
    if request.method=='POST':
        try:
            username=request.POST['username']
            print(username)
            password=request.POST['password']
            print(password)
            obj=Register.objects.get(email_phone=username,password=password)
            print(obj)
            request.session['ses']=obj.id
            obj1=Register.objects.get(id=obj.id)
            print(obj1)
            return render(request,'dashboard.html',{'msgobj':obj1})
        except Exception as e:print(e)
    return render(request, 'index.html',{'msginvalid':'invalid username or password'})


def fun2(request):
    return render(request, 'student.html')


def fun3(request):
    return render(request, 'staff.html')


def fun4(request):
    return render(request, 'home.html')


def fun5(request):
    return render(request, 'base.html')


def fun6(request):
    # try:
    #     if request.method == 'POST':
    #         fname = request.POST['fname']
    #         print(fname)
    #         lname = request.POST['surname']
    #         email = request.POST['email']
    #         password = request.POST['password']
    #         day = request.POST['day']
    #         month = request.POST['month']
    #         year = request.POST['year']
    #         dob = year+'-'+month+'-'+day
    #         gender = request.POST['gender']
    #         print(gender)
    #         obj1 = Register(firstname=fname, surname=lname, email_phone=email,
    #                         password=password, dob=dob, gender=gender)
    #         obj1.save()
    # except Exception as e:print(e)
    try:
        if request.method == 'POST':
            firstname = request.POST['fname']
            surname = request.POST['surname']
            mailid = request.POST['email']
            object2 = Register.objects.filter(email_phone=mailid).exists()
            if(object2 == False):
                pwd = request.POST['password']
                day = request.POST['day']
                month = request.POST['month']
                year = request.POST['year']
                dob = year+'-'+month+'-'+day
                gender = request.POST['gender']
                object1 = Register(firstname=firstname, surname=surname, email_phone=mailid,
                                   password=pwd, dob=dob, gender=gender)
                object1.save()
                return render(request,'index.html',{"msg":"account created successfully"})
            else:
                return render(request,'index.html',{"msg":"email already Exists"})
    except Exception as e:
        print(e)
    return render(request, 'index.html')


def fun7(request):
    if request.method=='POST':
        try:
            oldpass=request.POST['oldpassword']
            print(oldpass)
            newpass=request.POST['newpassword']
            print(newpass)
            obj3=request.session['ses']
            print(obj3)
            obj4=Register.objects.get(id=obj3)
            print(obj4)
            if obj4.password==oldpass:
                obj4.password=newpass
                obj4.save()
                return render(request,'changepassword.html',{'msge':'password changed succesfully'})
            return render(request,'changepassword.html',{'msg4':'old password is wrong'})  
        except Exception as e:print(e)
    return render(request, 'changepassword.html')


def fun8(request):
    if request.method=='POST':
        try:
            fname=request.POST['fname']
            sname=request.POST['sname']
            email=request.POST['email']
            day=request.POST['day']
            month=request.POST['month']
            year=request.POST['year']
            dateofbirth=year+'-'+month+'-'+day
            ob=request.session['ses']
            ob1=Register.objects.get(id=ob)
            ob1.firstname=fname
            ob1.surname=sname
            ob1.email_phone=email
            ob1.dob=dateofbirth
            ob1.save()
            return render(request,'editprofile.html',{'msms':'updated successfully'})
        except Exception as e:print(e)
    return render(request,'editprofile.html',{'msmsm':'something went wrong'})

