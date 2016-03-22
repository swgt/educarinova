from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from educarinova.management.models import Student, School
from educarinova.management.forms import StudentForm


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
def edit(request, pk):
    return render(request, 'management/students/student_edit.html')


@login_required
def new(request):
    form = StudentForm()
    return render(request, 'management/students/student_edit.html', {'form': form})


def delete():
    pass

def test_students(request, school):
    students = Student.objects.filter(school=school)
    print (students)
    return render(request, 'management/index.html', {'students': students})


def test_home(request):
    schools = School.objects.all()
    return render(request, 'management/home.html', {'schools': schools})