from django import forms
from .models import Restaraunt

class RestarauntForm(forms.ModelForm):
	class Meta:
		model = Restaraunt
		fields = ['name', 'description']