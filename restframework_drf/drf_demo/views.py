from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Employee

def index(request, a, b):
    add = int(a) + int(b)
    return JsonResponse({"data": add}, safe=False)


class EmployeesViews(viewsets.ModelViewSet):
    def get(request):
        queryset = Employee.objects.all()
        return JsonResponse({'data': 'abc'},safe=False)