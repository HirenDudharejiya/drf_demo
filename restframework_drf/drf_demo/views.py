from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Employee
from django.core import serializers
import json
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import datetime
import jwt
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

# access_token_payload = {
#     'user_id': user.id,
    # 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
    # 'iat': datetime.datetime.utcnow(),
#     'email': user.email
# }
# access_token = jwt.encode(access_token_payload,
#                           settings.SECRET_KEY, algorithm='HS256')
    # return access_token

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'email': user.email
    }

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            # login(request, user)
            user_auth = get_tokens_for_user(user)
            return JsonResponse(user_auth, safe=False)


def index(request, a, b):
    add = int(a) + int(b)
    return JsonResponse({"data": add}, safe=False)

def serializer_func(request):
    emp_object = Employee.objects.all()
    data = serializers.serialize('json', emp_object)
    print(json.loads(data))
    return JsonResponse({"data": json.loads(data)}, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_employee_list(request):
    employees = Employee.objects.all()
    employees = serializers.serialize('json', employees)
    return JsonResponse({"data": json.loads(employees)}, safe=False) 

class EmployeesViews(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    def list(self, request):
        serializer_data = EmployeeSerializer(self.queryset, many=True)
        return Response({"data": serializer_data.data})
    
    @staticmethod
    def combine_name(first_name, last_name):
        return first_name + " " + last_name
    
    @classmethod
    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=201)
    
    def retrieve(self, request, id=None):
        queryset = Employee.objects.filter(id=id)
        employee = get_object_or_404(queryset, id=id)
        serializer = EmployeeSerializer(employee)
        full_name = self.combine_name(employee.first_name, employee.last_name)
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
