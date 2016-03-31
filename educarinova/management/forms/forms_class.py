from django import forms
from educarinova.management.models import Class


class ClassForm(forms.ModelForm):

	class Meta:
		model = Class
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            'serie': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'}),
            'ano_letivo': forms.NumberInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            'unit': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'})
	            
        }