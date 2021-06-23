from django.urls import path
from .views import EmployeeRegisterView, EmployeeEditView, EmployeeView

urlpatterns = [
    path('register/', EmployeeRegisterView.as_view(), name='register'),
    path('edit/', EmployeeEditView.as_view(), name='edit'),
    path('employees/', EmployeeView.as_view(), name='employee'),
]

