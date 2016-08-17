from django import forms
from educarinova.management.models import SystemClass


class SystemClassForm(forms.ModelForm):

    class Meta:
        model = SystemClass
        fields = '__all__'
        widgets = {
  			# 'name': forms.TextInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            # 'serie': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'}),
            # 'ano_letivo': forms.NumberInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            #'start_time': forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
            # 'unit': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'})
        }