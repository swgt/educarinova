from django import forms
from educarinova.management.models import Serie


class SerieForm(forms.ModelForm):

	class Meta:
		model = Serie
		fields = '__all__'
		widgets = {
			'serie': forms.TextInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            
        }