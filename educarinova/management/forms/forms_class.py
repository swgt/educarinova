from django import forms
from educarinova.management.models import Class


class ClassForm(forms.ModelForm):

	class Meta:
		model = Class
		fields = '__all__'
		widgets = {
            'serie': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'}),
            'unit': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'}),
            'period': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'}),
            'shift': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'}),
	            
        }