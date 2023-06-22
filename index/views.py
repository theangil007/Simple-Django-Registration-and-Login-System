from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.


def registerpageview(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        # Check if the form is valid
        myuser = register.objects.filter(Email=email)

        if myuser:
            message = "Email is already registered !!"
            return render(request, "register.html", {"msg": message})
        else:
            if password == cpassword:
                myuser = register.objects.create(
                    Fullname=fullname, Email=email, Password=password
                )
                message = "User register Successfully."
                return render(request, "index.html", {"msg": message})

            else:
                message = "Password and confirm password doesn't match"
                return render(request, "register.html", {"msg": message})

    return render(request, "register.html")


def indexpageview(request):
    return render(request, "index.html")


def dashboardpageview(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Checking the email id in the database
            myuser = register.objects.get(Email=email)

            if myuser.Password == password:
                # Store user data in session
                request.session["Fullname"] = myuser.Fullname
                request.session["Email"] = myuser.Email
                return render(request, "dashboard.html")
            else:
                message = "Password doesn't match"
                return render(request, "index.html", {"msg": message})

        except register.DoesNotExist:
            message = "User doesn't exist."
            return render(request, "register.html", {"msg": message})

    return render(request, "dashboard.html")
