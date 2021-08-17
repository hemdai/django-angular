from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


from .models import Department, Employee
from .serializers import DepartmentSerializer, EmplyeeSerializer

# Create your views here.


@csrf_exempt
# @api_view(["POST", "GET", "PUT", "DELETE"])
def department_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            department_qs = Department.objects.all()
            department_serializer = DepartmentSerializer(department_qs, many=True)
            return JsonResponse(department_serializer.data, safe=False)
        else:
            try:
                department_qs = Department.objects.get(id=id)
            except Exception as er:
                return JsonResponse({"error": "not found object"}, safe=False)
            department_serializer = DepartmentSerializer(department_qs)
            return JsonResponse(department_serializer.data, safe=False)

    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(
            {
                "message": "failuer",
            },
            safe=False,
        )

    elif request.method == "PUT":
        if id != 0:
            department_data = JSONParser().parse(request)
            department_qs = Department.objects.get(id=id)
            serializer_data = DepartmentSerializer(department_qs, data=department_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse("Update Scucessfully", safe=False)
        return JsonResponse("Data not Valid", safe=False)

    elif request.method == "DELETE":
        if id != 0:
            department_qs = Department.objects.get(id=id).delete()
            return JsonResponse("Deleted Successfully", safe=False)
        return JsonResponse("Not Valid", safe=False)


@csrf_exempt
# @api_view(["POST", "GET", "PUT", "DELETE"])
def employee_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            employee_qs = Employee.objects.all()
            employee_serializer = EmplyeeSerializer(employee_qs, many=True)
            return JsonResponse(employee_serializer.data, safe=False)
        else:
            try:
                employee_qs = Employee.objects.get(id=id)
            except Exception as er:
                return JsonResponse({"error": "not found object"}, safe=False)
            employee_serializer = EmplyeeSerializer(employee_qs)
            return JsonResponse(employee_serializer.data, safe=False)

    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        department = Department.objects.get(id=employee_data["department"])
        # employee_data["department"] = department
        employee_serializer = EmplyeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(
            {
                "message": "failuer",
            },
            safe=False,
        )

    elif request.method == "PUT":
        if id != 0:
            employee_data = JSONParser().parse(request)
            employee_qs = Employee.objects.get(id=id)
            serializer_data = EmplyeeSerializer(employee_qs, data=employee_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse("Update Scucessfully", safe=False)
        return JsonResponse("Data not Valid", safe=False)

    elif request.method == "DELETE":
        if id != 0:
            employee_qs = Department.objects.get(id=id).delete()
            return JsonResponse("Deleted Successfully", safe=False)
        return JsonResponse("Not Valid", safe=False)
