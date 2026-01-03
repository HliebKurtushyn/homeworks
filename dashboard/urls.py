from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.register, name='dashboard_home'),
]