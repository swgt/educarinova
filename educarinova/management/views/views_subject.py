from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from educarinova.management.models import Subject
from educarinova.management.forms.forms_subjects import SubjectForm

@login_required
def list_subject(request):
    subjects = Subject.objects.all().order_by('-id')
    return render(request, 'management/subject/subject_list.html', {'subjects': subjects})

@login_required
def new_subject(request):
    
	if request.method == 'POST':
		formSubject = SubjectForm(request.POST)
		if (formSubject.is_valid()):
			subject = formSubject.save(commit=False)
			subject.save()

			return redirect('/subject?op=success', pk='teste')
		else:
			return render(request, 'management/subject/subject_edit.html', {'form': formSubject})
	else:
		form = SubjectForm()
		return render(request, 'management/subject/subject_edit.html', {'form': form})