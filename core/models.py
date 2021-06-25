from django.db import models
#from django.contrib.auth.models import Employee
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField

from accounts.models import Employee

from datetime import datetime, date

# Create your models here.

class News(models.Model):
	TYPES = [
		('สั่งการ', 'สั่งการ'),
		('ประชาสัมพันธ์', 'ประชาสัมพันธ์')
	]
	type = models.CharField(max_length=50, choices=TYPES, default='สั่งการ')
	date_published = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=200)
	#detail = models.TextField()
	detail = RichTextField()
	author = models.ForeignKey(Employee, on_delete=models.CASCADE)
	read = models.ManyToManyField(Employee, related_name='read_newss')

	def __str__(self):
		return self.type + ' | ' + str(self.date_published) + ' | ' + self.name + ' | ' + str(self.author)

	def get_absolute_url(self):
	    return reverse_lazy("home")
	

