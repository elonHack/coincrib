from django.shortcuts import render
import random
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect as redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'homepage/html/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(user,request)
            return redirect("You are logged in " + str(request.POST.email))
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        userName = fname[0].lower() + lname.lower() + '0' + str(random.randrange(0, 9999))
        email = request.POST["email"]
        password = request.POST["passwd"]
        check_box = request.POST["check"]

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Address Already Exists")
            return redirect(reverse('signup-page'))
        elif check_box != 'on':
            messages.info(request, "You need to accept the terms and conditions")
            
        else:
            user = User.objects.create_user(username=userName, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            messages.info(request, 'User Created')
            return redirect(reverse('login-page'))
    return render(request, 'registration/signup.html')

def logout(request):
    pass


