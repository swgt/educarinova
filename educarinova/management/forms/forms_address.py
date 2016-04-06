from django import forms
from educarinova.management.models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
  #         'name': forms.TextInput(attrs={'class': 'form-control', 'aria-required':'true'}),
            'type_of_street': forms.Select(attrs={'data-init-plugin':'select2'}),
         #   'ano_letivo': forms.NumberInput(attrs={'class': 'form-control', 'aria-required':'true'}),
          #  'unit': forms.Select(attrs={'class':'form-control','data-init-plugin':'select2'})

        }