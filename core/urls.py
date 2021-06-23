from django.urls import path

from .views import HomeView, NewsDetailView, AddNewsView, UpdateNewsView, DeleteNewsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news/add/', AddNewsView.as_view(), name='add_news'),
    path('news/edit/<int:pk>', UpdateNewsView.as_view(), name='update_news'),
    path('news/<int:pk>/remove/', DeleteNewsView.as_view(), name='delete_news'),
]
