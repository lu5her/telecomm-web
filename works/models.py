from django.db import models
from django.urls import reverse_lazy

from accounts.models import Employee

# Create your models here.

class Work(models.Model):
	TYPES = [
		('ดาต้า', 'ดาต้า'),
		('ลิ้งค์', 'ลิงค์'),
		('ดาวเทียม', 'ดาวเทียม'),
		('วงรอบ', 'วงรอบ'),
		('เอกสาร', 'เอกสาร'),
		('อื่น ๆ', 'อื่น ๆ')
	]
	work_date = models.DateField(auto_now_add=True)
	type = models.CharField(max_length=20, choices=TYPES, default='อื่น ๆ')
	name = models.CharField(max_length=200)
	detail = models.CharField(max_length=200)
	worker = models.ForeignKey(Employee, on_delete=models.CASCADE)

	def __str__(self):
		return self.type + ' | ' + str(self.work_date) + ' | ' + self.name + ' | ' + str(self.worker)

	def get_absolute_url(self):
	    return reverse_lazy("work")
	
