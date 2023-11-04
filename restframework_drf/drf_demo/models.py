from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    date_of_joining = models.DateField(default=datetime.datetime.now())
    leaves = models.FloatField()
    active = models.BooleanField(default=True)
