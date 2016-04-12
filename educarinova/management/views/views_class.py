from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from educarinova.management.models import Class
from educarinova.management.forms.forms_class import ClassForm

@login_required
def list_class(request):
    classes = Class.objects.all().order_by('-id')
    return render(request, 'management/class/class_list.html', {'classes': classes})

@login_required
def new_class(request):
    
	if request.method == 'POST':
		formClass = ClassForm(request.POST)
		if (formClass.is_valid()):
			vclass = formClass.save(commit=False)
			vclass.save()


			return redirect('/subject?op=success', pk='teste')
		else:
			return render(request, 'management/class/class_edit.html', {'form': formClass})
	else:
		form = ClassForm()
		return render(request, 'management/class/class_edit.html', {'form': form})