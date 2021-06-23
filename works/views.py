from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Work
from .forms import WorkForm, WorkUpdateForm

# Create your views here.

class WorkView(ListView):
	model = Work
	template_name = 'works/work.html'

class WorkDetailView(DetailView):
	model = Work
	template_name = 'works/work_detail.html'

class WorkAddView(CreateView):
	model = Work
	form_class = WorkForm
	template_name = 'works/work_add.html'

class WorkUpdateView(UpdateView):
	model = Work
	form_class = WorkUpdateForm
	template_name = 'works/work_update.html'
	success_url = reverse_lazy('work')

class WorkDeleteView(DeleteView):
	model = Work
	template_name = 'works/work_delete.html'
	success_url = reverse_lazy('work')

