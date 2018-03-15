from django.db import models

# Create your models here.
class Salary(models.Model):
    gross_income = models.IntegerField()
    basic = models.IntegerField()
    overtime = models.IntegerField()
