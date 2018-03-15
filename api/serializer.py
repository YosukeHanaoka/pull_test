# coding: utf-8

from rest_framework import serializers

from .models import Salary


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('gross_income', 'basic', 'overtime')
