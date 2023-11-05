from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User



class EmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    salary = serializers.FloatField()
    date_of_joining = serializers.DateField(error_messages={'required': 'Custom error message'})
    leaves = serializers.FloatField()
    active = serializers.BooleanField(default=True)

    class Meta: 
        model = Employee
        fields = "__all__"
        # exclude = ('salary', )