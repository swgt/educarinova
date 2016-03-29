from django import forms
from educarinova.management.models import Unit


class UnitForm(forms.ModelForm):

	class Meta:
		model = Unit
		fields = '__all__'