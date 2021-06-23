from django.urls import path

from .views import WorkView, WorkDetailView, WorkAddView, WorkUpdateView, WorkDeleteView

urlpatterns = [
    path('', WorkView.as_view(), name='work'),
    path('add/', WorkAddView.as_view(), name='work_add'),
    path('detail/<int:pk>/', WorkDetailView.as_view(), name='work_detail'),
    path('update/<int:pk>/', WorkUpdateView.as_view(), name='work_update'),
    path('<int:pk>/remove/', WorkDeleteView.as_view(), name='work_delete'),

]
