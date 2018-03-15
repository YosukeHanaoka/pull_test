from django.shortcuts import render

# Create your views here.
import django_filters
from rest_framework import viewsets, filters

from .models import Salary
from .serializer import SalarySerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
