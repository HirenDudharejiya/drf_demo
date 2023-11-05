from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Employee
from django.core import serializers
import json
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


def index(request, a, b):
    add = int(a) + int(b)
    return JsonResponse({"data": add}, safe=False)

def serializer_func(request):
    emp_object = Employee.objects.all()
    data = serializers.serialize('json', emp_object)
    print(json.loads(data))
    return JsonResponse({"data": json.loads(data)}, safe=False)


class EmployeesViews(viewsets.ViewSet):
    queryset = Employee.objects.all()
    def list(self, request):
        serializer_data = EmployeeSerializer(self.queryset, many=True)
        return Response({"data": serializer_data.data})

    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=201)
    
    def retrieve(self, request, id=None):
        queryset = Employee.objects.filter(id=id)
        employee = get_object_or_404(queryset, id=id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=200)

    def update(self, request, id, *args, **kwargs):
        instance = Employee.objects.filter(id=id).first()
        serializer = EmployeeSerializer(instance, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({"data": serializer.data})

    def partial_update(self, request, id=None, *args, **kwargs):
        instance = Employee.objects.filter(id=id).first()
        serializer = EmployeeSerializer(instance, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response({"data": serializer.data})

    def destroy(self, request, id=None):
        serializer = Employee.objects.filter(id=id)
        serializer.delete()
        return Response({'data': "Successfully deleted"})
