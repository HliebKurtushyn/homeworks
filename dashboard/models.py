from django.db import models
from account.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=100, default="dashboard/default.png")

    def __str__(self):
        return self.name
    
User.add_to_class('courses', models.ManyToManyField(Course, blank=True))