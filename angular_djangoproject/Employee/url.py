from django.urls import path, include
from .views import department_api, employee_api

urlpatterns = [
    path("department/", department_api, name="department"),
    path("department/<int:id>", department_api, name="department-unique"),
    path("employee/", employee_api, name="employee"),
    path("employee<int:id>", employee_api, name="employee-unique"),
]
