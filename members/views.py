from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method=="POST":
        username = request.POST['Username']
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,("there was an error login in try again"))
            return redirect('login')

    
    return render(request,'authenticate/login.html')

