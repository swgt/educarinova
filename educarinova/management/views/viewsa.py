from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r, redirect
from educarinova.management.models import Student
from django.contrib.auth.models import User
from educarinova.management.forms.forms_students import StudentForm, AddressForm, UserForm, ContactForm


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
        'form_user': UserForm()
    })


@login_required
def create(request):
    form_student = StudentForm(request.POST)

    if not form_student.is_valid():

        return render(request, 'management/students/student_edit.html', {'form_student': form_student})

    student = Student.objects.create(**form_student.cleaned_data)

    return HttpResponseRedirect(r('students:detail', student.pk))


@login_required
def detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        raise Http404

    return render(request, 'management/students/student_detail.html', {'student': student})