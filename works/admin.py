from django.contrib import admin

from .models import Work

# Register your models here.



class WorkList(admin.ModelAdmin):
	model = Work
	list_display = ['name', 'type', 'worker', 'work_date']
	
admin.site.register(Work, WorkList)