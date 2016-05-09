from django import forms
from educarinova.management.models import Student, Address, Matriculation, Contact, TuitionFee, Responsible, ResponsibleStudent
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control datepicker-component2'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'dispatch_entity_rg': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'nationality': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'race': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'naturalness': forms.TextInput(attrs={'class': 'form-control'}),
            'matriculation': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('__all__')
        widgets = {
            'type_of_street': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'complement': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
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
            'school_class': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
        }


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('__all__')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class TuitionFeeForm(forms.ModelForm):

    class Meta:
        model = TuitionFee
        fields = ('__all__')
        widgets = {
            'frequency_payment': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'expiration_day': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
            'discount_tuition_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'reason_discount_tuition_fee': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ResponsibleForm(forms.ModelForm):

    class Meta:
        model = Responsible
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ResponsibleStudentForm(forms.ModelForm):

    class Meta:
        model = ResponsibleStudent
        fields = ('__all__')
        widgets = {
            'kinship': forms.Select(attrs={'class': 'full-width', 'data-init-plugin': 'select2'}),
        }