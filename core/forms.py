from django import forms
from django.forms import fields, widgets


from .models import News


class NewsForm(forms.ModelForm):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		TYPES = [
			('สั่งการ', 'order'),
			('ประชาสัมพันธ์', 'announce')
		]
		model = News
		fields = ('type', 'name', 'detail', 'file', 'author')
		#exlude = 'date_published'
		labels = {
                    'type': 'ประเภท',
                				'name': 'ชื่อเรื่อง',
                				'detail': 'รายละเอียด',
						'file': 'อัพโหลดไฟล์',
                				'author': 'สร้างโดย'
                }
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'type': forms.Select(choices=TYPES, attrs={'class': 'form-control'}),
			'detail': forms.Textarea(attrs={'class': 'form-control'}),
			#'file': forms.FileField(widgets.ClearableFileInput ,attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'type': 'hidden'})
                }


class EditForm(forms.ModelForm):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		TYPES = {
			'สั่งการ': 'order',
		    	'ประชาสัมพันธ์': 'announce'
	    	}
		model = News
		fields = ('type', 'name', 'detail', 'file')
	    	#exlude = 'date_published'
		labels = {
			'type': 'ประเภท',
			'name': 'ชื่อเรื่อง',
			'detail': 'รายละเอียด',
			'file': 'อัพโหลดไฟล์',
	    	}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'detail': forms.Textarea(attrs={'class': 'form-control'}),
			#'file': forms.FileField(widgets.ClearableFileInput ,attrs={'class': 'form-control'}),
	    	}
