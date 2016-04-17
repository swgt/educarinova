from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r, redirect
from educarinova.management.models import Student, Contact, Address, Matriculation, TuitionFee
from django.contrib.auth.models import User
from educarinova.management.forms.forms_students import StudentForm, AddressForm, UserForm, ContactForm, MatriculationForm, TuitionFeeForm


def register(request):
    return render(request, 'registration/register.html')


@login_required
def dashboard(request):
    return render(request, 'management/dashboard.html')


@login_required
def list_(request):
    students = Student.objects.all()
    return render(request, 'management/students/students_list.html', {'students': students})


@login_required
def delete():
    pass


@login_required
def edit():
    pass


@login_required
def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


@login_required
def empty_form(request):
    return render(request, 'management/students/student_edit.html', {
        'form_student': StudentForm(),
        'form_address': AddressForm(),
        'form_contact': ContactForm(),
        'form_user': UserForm(),
        'form_matriculation': MatriculationForm(),
        'form_tuition_fee': TuitionFeeForm(),
    })


@login_required
def create(request):
    form_student = StudentForm(request.POST)
    form_address = AddressForm(request.POST)
    form_contact = ContactForm(request.POST)
    form_matriculation = MatriculationForm(request.POST)
    form_tuition_fee = TuitionFeeForm(request.POST)

    print(">>>>>>>>>>>>>>" + str(form_matriculation.errors))

    if not form_student.is_valid() or not form_address.is_valid() or not form_contact.is_valid() \
            or not form_matriculation.is_valid() or not form_tuition_fee.is_valid():
        return render(request, 'management/students/student_edit.html', {'form_student': form_student,
                                                                         'form_address': form_address,
                                                                         'form_contact': form_contact,
                                                                         'form_matriculation': form_matriculation,
                                                                         'form_tuition_fee': form_tuition_fee})

    cpf = form_student.cleaned_data['cpf']
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    form_student.cleaned_data['cpf'] = cpf

    address = Address.objects.create(**form_address.cleaned_data)
    contact = Contact.objects.create(**form_contact.cleaned_data)
    student = Student.objects.create(**form_student.cleaned_data)
    student.address = address
    student.contact = contact
    student.save()

    matriculation = Matriculation.objects.create(**form_matriculation.cleaned_data)
    tuition_fee = TuitionFee.objects.create(**form_tuition_fee.cleaned_data)
    matriculation.student = student
    matriculation.tuition_fee = tuition_fee
    matriculation.save()

    return HttpResponseRedirect(r('students:detail', student.pk))


@login_required
def detail(request, pk):
    try:
        form_student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        raise Http404

    return render(request, 'management/students/student_detail.html', {'form_student': form_student})