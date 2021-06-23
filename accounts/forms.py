from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets

from .models import Employee

class EmployeeCreationForm(UserCreationForm):
	#password = forms.CharField(attrs={'class': 'form-control'})
	class Meta:
		model = Employee
		fields = ('rank', 'first_name', 'last_name', 'position', 'sector', 'place', 'phone', 'email', 'username')
		#fields = '__all__'
		labels = {
			'username': 'ชื่อเข้าใข้งาน',
			#'password1': 'รหัสผ่าน',
			#'password2': 'ยืนยันรหัสผ้าน',
			'rank': 'ยศ',
			'first_name': 'ชื่อ',
			'last_name': 'นามสกุล',
			'position': 'ตำแหน่ง',
			'sector': 'สังกัด',
			'place': 'หน่วย',
			'phone': 'หมายเลขโทรศัพท์',
			'email': 'อีเมลล์'
		}
		widgets = {
			'rank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น จ.ส.ต., ส.อ.'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'position': forms.TextInput(attrs={'class': 'form-control'}),
			'sector': forms.Select(attrs={'class': 'form-control'}),
			'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น สทค.มทบ...'}),
			'phone': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'})

		}


class EmployeeChangeForm(UserChangeForm):
	class Meta:
		model = Employee
		fields = ('rank', 'first_name', 'last_name', 'position', 'sector', 'place', 'phone', 'email')