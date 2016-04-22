from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from educarinova.management.models import Student, Contact, Address, Matriculation, TuitionFee, Class
from educarinova.management.forms.forms_students import StudentForm, AddressForm, UserForm, ContactForm, \
    MatriculationForm, TuitionFeeForm


@login_required
def list_(request):
    students = Student.objects.all()
    return render(request, 'management/students/students_list.html', {'students': students})


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

    if not form_student.is_valid() or not form_address.is_valid() or not form_contact.is_valid() \
            or not form_matriculation.is_valid() or not form_tuition_fee.is_valid():
        return render(request, 'management/students/student_edit.html',
                      {'form_student': form_student,
                       'form_address': form_address,
                       'form_contact': form_contact,
                       'form_matriculation': form_matriculation,
                       'form_tuition_fee': form_tuition_fee})

    form_student.cleaned_data['cpf'] = _remove_mask_field(form_student.cleaned_data['cpf'])
    form_contact.cleaned_data['cell_phone'] = _remove_mask_field(form_contact.cleaned_data['cell_phone'])
    form_address.cleaned_data['cep'] = _remove_mask_field(form_address.cleaned_data['cep'])

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

    return redirect('students:detail', student.pk)


@login_required
def detail(request, pk):
    form_student = get_object_or_404(Student, pk=pk)

    return render(request, 'management/students/student_detail.html', {'form_student': form_student})


@login_required
def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form_student = StudentForm(request.POST, instance=student)
        if form_student.is_valid():
            student = form_student.save(commit=False)
            student.save()
            return redirect('students:detail', student.pk)
    else:
        form_student = StudentForm(instance=student)
    return render(request, 'management/students/student_edit.html', {'form_student': form_student})


@login_required
def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()

    return redirect('students:list')


def _remove_mask_field(field):
    values = (('.', ""),
              ('-', ""),
              ('(', ""),
              (')', ""))

    for out, _in in values:
        field = field.replace(out, _in)

    return field


def filter_by_class(request):
    pk_class = request.POST.get('pk_school_class')
    class_ = get_object_or_404(Class, pk=pk_class)

    return HttpResponse(class_.value_tuition_fee)