from django import forms
from educarinova.management.models import Subject


class SubjectForm(forms.ModelForm):

	class Meta:
		model = Subject
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
        }