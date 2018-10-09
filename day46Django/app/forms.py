# Filename  : forms.py
# Date  : 2018/9/17
from django import forms


class UserForm(forms.Form):

	username = forms.CharField(required=True)
	password = forms.CharField(required=True)