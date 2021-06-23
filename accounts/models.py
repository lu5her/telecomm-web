from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class Employee(AbstractUser):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	rank = models.CharField(max_length=20)
	#first_name = models.CharField(max_length=200)
	#last_name = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	sector = models.CharField(max_length=100, choices=[
		('ส่วนกลาง', 'ส่วนกลาง'),
		('ทภ.1', 'ทภ.1'),
		('ทภ.2', 'ทภ.2'),
		('ทภ.3', 'ทภ.3'),
		('ทภ.4', 'ทภ.4'),
		('อื่นๆ', 'อื่นๆ')
	])
	place = models.CharField(max_length=200)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	
