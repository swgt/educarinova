from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from educarinova.management.models import Student, Contact, Address, Matriculation, TuitionFee, Class, Responsible, \
    ResponsibleStudent, ClassSystemClass
from educarinova.management.forms.forms_students import StudentForm, AddressForm, UserForm, ContactForm, \
    MatriculationForm, TuitionFeeForm, ResponsibleForm, ResponsibleStudentForm


@login_required
def list_(request):
    query = request.GET.get('q')
    if query is None:
        query = ''

    total_students = Student.objects.count()
    students_active = Student.objects.filter(status__exact="info")
    student_list = students_active.filter(Q(name__icontains=query) |
                                          Q(cpf__icontains=query) |
                                          Q(contact__email__icontains=query) |
                                          Q(date_of_birth__icontains=query)).order_by('created_at')

    paginator = Paginator(student_list, 10)

    page = request.GET.get('page')

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'management/students/students_list.html',
                  {'students': students,
                   'query': query,
                   'total_students': total_students})


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
        'form_responsible': ResponsibleForm(),
        'form_responsible_student': ResponsibleStudentForm(),
        'form_tuition_fee': TuitionFeeForm(),
    })


@login_required
def create(request):
    form_student = StudentForm(request.POST)
    form_address = AddressForm(request.POST)
    form_contact = ContactForm(request.POST)
    form_matriculation = MatriculationForm(request.POST)
    form_responsible = ResponsibleForm(request.POST)
    form_responsible_student = ResponsibleStudentForm(request.POST)
    form_tuition_fee = TuitionFeeForm(request.POST)

    if not form_student.is_valid() or not form_address.is_valid() or not form_contact.is_valid() \
            or not form_matriculation.is_valid() or not form_responsible.is_valid() \
            or not form_responsible_student.is_valid() or not form_tuition_fee.is_valid():
        return render(request, 'management/students/student_edit.html',
                      {'form_student': form_student,
                       'form_address': form_address,
                       'form_contact': form_contact,
                       'form_matriculation': form_matriculation,
                       'form_responsible': form_responsible,
                       'form_responsible_student': form_responsible_student,
                       'form_tuition_fee': form_tuition_fee})

    form_student.cleaned_data['cpf'] = _remove_mask_field(form_student.cleaned_data['cpf'])
    form_contact.cleaned_data['cell_phone'] = _remove_mask_field(form_contact.cleaned_data['cell_phone'])
    form_address.cleaned_data['cep'] = _remove_mask_field(form_address.cleaned_data['cep'])

    address = Address.objects.create(**form_address.cleaned_data)
    contact = Contact.objects.create(**form_contact.cleaned_data)
    student = Student.objects.create(**form_student.cleaned_data)
    responsible = Responsible.objects.create(**form_responsible.cleaned_data)
    student.address = address
    student.contact = contact
    student.save()

    matriculation = Matriculation.objects.create(**form_matriculation.cleaned_data)
    tuition_fee = TuitionFee.objects.create(**form_tuition_fee.cleaned_data)
    matriculation.student = student
    matriculation.tuition_fee = tuition_fee
    matriculation.save()

    responsible_student = ResponsibleStudent.objects.create(**form_responsible.cleaned_data)
    responsible_student.student = student
    responsible_student.responsible = responsible
    responsible_student.save()

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
def delete(request):
    for pk in request.POST:
        if pk != 'csrfmiddlewaretoken':
            student = get_object_or_404(Student, pk=pk)
            student.status = 'danger'
            student.save()

    return redirect('students:list')


def filter_by_class(request):
    pk_class = request.POST.get('pk_school_class')
    class_system_class = get_object_or_404(ClassSystemClass, classv=pk_class)

    return HttpResponse(class_system_class.value_tuition_fee)


def _remove_mask_field(field):
    values = (('.', ""),
              ('-', ""),
              ('(', ""),
              (')', ""))

    for out, _in in values:
        field = field.replace(out, _in)

    return field
