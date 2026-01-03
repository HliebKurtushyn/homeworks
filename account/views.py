from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard_home")
    else:
        form = StudentRegistrationForm()
    
    return render(request, "account/register.html", {"form": form})
