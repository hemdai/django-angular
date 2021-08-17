from django.db import models
import datetime

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now_add=True, blank=True)
    photo_file_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
