from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def login_(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('cart')
        else:
            return render(request,'login.html',{'wc':True})

    return render(request,'login.html',{'about':True})


def register(request):

    if request.method == 'POST':
        first_name=request.POST['name']

        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create(first_name=first_name,email=email,username=username)
        user.set_password(password)
        user.save()
        return redirect('login_')


    return render(request,'register.html',{'about':True})

def logout_(request):

    logout(request)
    return redirect ('home')