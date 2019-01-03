from django import forms
from .models import firstapp_model


class Firstapp_forms(forms.ModelForm):

	class Meta:
		model = firstapp_model
		fields = ('name', 'age')