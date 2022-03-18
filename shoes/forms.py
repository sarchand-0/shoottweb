from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
	class Meta:
		model=OrderItem
		fields='__all__'


class CreateUserForm(UserCreationForm):
	phone =  forms.CharField(max_length=200)
	country = forms.CharField(max_length=200)
	city = forms.CharField(max_length=200)
	street = forms.CharField(max_length=200)


	class Meta:
		model=User
		fields=[ 'username', 'email', 'password1', 'password2', 'phone', 'country', 'city', 'street' ]

class ContactForm(ModelForm):
	message = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model=Contact
		fields=['name','email','message']



