from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Course

@login_required
def home_view(request):
    user_courses = request.user.courses.all()
    user = request.user

    return render(request, "dashboard/home.html", {"courses": user_courses, "user": user})