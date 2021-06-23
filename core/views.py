from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News
from .forms import NewsForm, EditForm

# Create your views here.

#def HomeView(request):
#    return render(request, 'home.html', {})

class HomeView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    redirect_field_name = 'home'
    model = News
    template_name = 'home.html'
    ordering = ['-date_published']

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

class AddNewsView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'add_news.html'


class UpdateNewsView(UpdateView):
    model = News
    form_class = EditForm
    template_name = 'update_news.html'
    success_url = reverse_lazy('home')

class DeleteNewsView(DeleteView):
    model = News
    form_class = EditForm
    template_name = 'delete_news.html'
    success_url = reverse_lazy('home')
