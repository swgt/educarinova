from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from educarinova.management.models import Class, Matriculation
from educarinova.management.forms.forms_class import ClassForm


@login_required
def list_class(request):
    query = request.GET.get('q')
    if query is None:
        query = ''

    total_classes = Class.objects.count()
    class_list = Class.objects.filter(Q(name__icontains=query) | Q(academic_year__icontains=query) |
                                          Q(shift__icontains=query)).order_by('-id')

    paginator = Paginator(class_list, 10)

    page = request.GET.get('page')

    try:
        classv = paginator.page(page)
    except PageNotAnInteger:
        classv = paginator.page(1)
    except EmptyPage:
        classv = paginator.page(paginator.num_pages)

    return render(request, 'management/class/class_list.html',
                  {'classes': classv,
                   'query': query,
                   'total_classes': total_classes})


@login_required
def detail_class(request, pk):
    form_class = get_object_or_404(Class, pk=pk)
    matriculations = Matriculation.objects.filter(school_class=pk)

    return render(request, 'management/class/class_detail.html', {'form_class': form_class,
                                                                  'matriculations': matriculations})


@login_required
def new_class(request):
    if request.method == 'POST':
        formClass = ClassForm(request.POST)
        if (formClass.is_valid()):
            vclass = formClass.save(commit=False)
            vclass.save()

            return redirect('/class?op=success', {'class':vclass})
        else:
            return render(request, 'management/class/class_edit.html', {'form': formClass})
    else:
        form = ClassForm()
        return render(request, 'management/class/class_edit.html', {'form': form})