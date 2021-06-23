from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import EmployeeCreationForm, EmployeeChangeForm
from .models import Employee
# Create your views here.

class EmployeeRegisterView(generic.CreateView):
	form_class = EmployeeCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class EmployeeEditView(generic.UpdateView):
	form_class = EmployeeChangeForm
	template_name = 'registration/edit.html'
	success_url = reverse_lazy('home')

	def get_object(self):
	    return self.request.user

class EmployeeView(LoginRequiredMixin, generic.ListView):
	login_url = 'login'
	redirect_field_name = 'home'
	model = Employee
	template_name = 'employee.html'