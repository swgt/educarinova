from django import forms
from educarinova.management.models import Classroom


class ClassroomForm(forms.ModelForm):

	class Meta:
		model = Classroom
		fields = ['unit', 'identification', 'type']
		widgets = {
			'unit': forms.Select(attrs={'class': 'form-control'}),
            'identification': forms.TextInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            
        }