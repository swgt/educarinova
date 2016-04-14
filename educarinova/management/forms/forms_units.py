from django import forms
from educarinova.management.models import Unit


class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ['name', 'school']
        widgets = {'school': forms.Select(attrs={'data-init-plugin': 'select2', 'class': 'form-group-select2'})}