from django import forms

from .models import Work


class WorkForm(forms.ModelForm):
	class Meta:
		TYPES = [
		('ดาต้า', 'ดาต้า'),
		('ลิ้งค์', 'ลิงค์'),
		('ดาวเทียม', 'ดาวเทียม'),
		('วงรอบ', 'วงรอบ'),
		('เอกสาร', 'เอกสาร'),
		('อื่น ๆ', 'อื่น ๆ')
	]
		model = Work
		fields = ('type', 'name', 'detail', 'worker')
		labels = {
			
			'type': 'ประเภทงาน',
			'name': 'ชื่องาน',
			'detail': 'รายละเอียด'
		}
		widgets = {
			
			'type': forms.Select(choices=TYPES, attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'detail': forms.Textarea(attrs={'class': 'form-control'}),
			'worker': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'type':'hidden'})
		}


class WorkUpdateForm(forms.ModelForm):
	class Meta:
		TYPES = [
		('ดาต้า', 'ดาต้า'),
		('ลิ้งค์', 'ลิงค์'),
		('ดาวเทียม', 'ดาวเทียม'),
		('วงรอบ', 'วงรอบ'),
		('เอกสาร', 'เอกสาร'),
		('อื่น ๆ', 'อื่น ๆ')
	]
		model = Work
		fields = ('type', 'name', 'detail')
		labels = {
			
			'type': 'ประเภทงาน',
			'name': 'ชื่องาน',
			'detail': 'รายละเอียด'
		}
		widgets = {
			
			'type': forms.Select(choices=TYPES, attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'detail': forms.Textarea(attrs={'class': 'form-control'})
			
		}