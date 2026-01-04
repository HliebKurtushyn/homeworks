from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, StudentAuthForm

from django.http import JsonResponse

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard_home")

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # login(request, user)
            # return redirect("dashboard_home")
            return JsonResponse({"register_status": "success"})
    else:
        form = StudentRegistrationForm()
    
    return render(request, "account/register.html", {"form": form})


def login_view(request):    
    if request.method == "POST":
        form = StudentAuthForm(request, data=request.POST)
        if form.is_valid():
            # login(request, form.get_user())
            # return redirect("dashboard_home")
            return JsonResponse({"login_status": "success"})
    else:
        form = StudentAuthForm()
    
    return render(request, "account/login.html", {"form": form})
