from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return {
                    "status": "success",
                    "redirect": "login"
                    }
    else:
        form = StudentRegistrationForm()
    
    return render(request, "account/register.html", {"form": form})
