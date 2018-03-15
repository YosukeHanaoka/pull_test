from django.contrib import admin

# Register your models here.
from .models import Salary

@admin.register(Salary)
class UserAdmin(admin.ModelAdmin):
    pass
