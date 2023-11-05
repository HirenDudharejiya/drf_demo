from django.urls import path
from . import views

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('index/<str:a>/<str:b>/', views.index, name="index"),
    path('employee/', views.EmployeesViews.as_view({'get': 'list', "post": 'create'}), name="employee"),
    path('employee/<str:id>/', views.EmployeesViews.as_view({'get': 'retrieve', 'delete': 'destroy', 
                                                             'put': 'update', 'patch': 'partial_update'}), name="employee"),
    path('serializer_func/', views.serializer_func),
]
