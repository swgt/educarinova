from django import forms
from educarinova.management.models import Student, Address, Matriculation, Contact


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('__all__')
        GENDERS = (
            ('M', 'Masculino'),
            ('F', 'Feminino'),
        )
        gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDERS)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control datepicker-component2'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'dispatch_entity_rg': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'nationality': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'race': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'naturalness': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'matriculation': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('__all__')
        widgets = {
            'type_of_street': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'complement': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
        widgets = {
            'cell_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'cell_phone_secondary': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_secondary': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MatriculationForm(forms.ModelForm):

    class Meta:
        model = Matriculation
        fields = ('__all__')
        widgets = {
            'number_matriculation': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'status': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
        }