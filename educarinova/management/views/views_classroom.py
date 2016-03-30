from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from educarinova.management.models import Classroom
from educarinova.management.forms.forms_classrooms import ClassroomForm

@login_required
def list_classroom(request):
    classrooms = Classroom.objects.all()
    return render(request, 'management/classroom/classroom_list.html', {'classrooms': classrooms})

@login_required
def new_classroom(request):
    form = ClassroomForm()
    return render(request, 'management/classroom/classroom_edit.html', {'form': form})