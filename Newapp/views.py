from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Newapp.forms import Loginregister, studentregform


# Create your views here.
def New(request):
    return render(request,"new.html")


def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("New")
            elif user.is_student:
                return redirect("New")
        else:
            messages.info(request, 'invalid Credentials')
    return render(request,"login.html")


def studentregbase(request):

    return render(request,"student/studentregbase.html")

def studentreg(request):
    form1 = Loginregister()
    form2 = studentregform()
    if request.method == "POST":
        form1 = Loginregister(request.POST)
        form2 = studentregform(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_student = True
            data.save()
            data1 = form2.save(commit=False)
            data1.user = data
            data1.save()
            return redirect("log")
    return render(request,"student/studentreg.html",{'form1': form1, 'form2': form2})