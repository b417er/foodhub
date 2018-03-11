from django import forms
from .models import Restaraunt, Item
from django.contrib.auth.models import User

def user_logout(request):
	logout(request)
	return redirect('login')


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()

		}

class RestarauntForm(forms.ModelForm):
	class Meta:
		model = Restaraunt
		fields = '__all__'

		widgets = {

		"opening": forms.TimeInput(attrs={'type':'time'}),
		"closing": forms.TimeInput(attrs={'type':'time'}),

		}


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ['restaraunt']
