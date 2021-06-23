from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeCreationForm, EmployeeChangeForm
from .models import Employee

# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = EmployeeCreationForm
	form = EmployeeChangeForm
	model = Employee
	list_display = ['username', 'first_name', 'last_name', 'email']

admin.site.register(Employee, CustomUserAdmin)