from django.db.models import fields
from rest_framework import serializers
from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmplyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("name", "department", "joining_date", "photo_file_name")
