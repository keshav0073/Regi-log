from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder': 'Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password must be contain 8 charc','autocomplete':'off'}))
	password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Repeat password'}))
	# first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	# last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'Number'}), required=False)




class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off','placeholder': 'Password'}))