from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from educarinova.management.models import SystemClass
from educarinova.management.forms.forms_systemclass import SystemClassForm


@login_required
def list_systemclass(request):
    query = request.GET.get('q')
    if query is None:
        query = ''

    total_systemclasses = SystemClass.objects.count()
    
    systemclass_list = SystemClass.objects.filter(Q(system__icontains=query)).order_by('-id')

    paginator = Paginator(systemclass_list, 10)

    page = request.GET.get('page')

    try:
        systemclass = paginator.page(page)
    except PageNotAnInteger:
        systemclass = paginator.page(1)
    except EmptyPage:
        systemclass = paginator.page(paginator.num_pages)

    return render(request, 'management/systemclass/systemclass_list.html',
                  {'systemclasses': systemclass,
                   'query': query,
                   'total_systemclasses': total_systemclasses})


@login_required
def detail_systemclass(request, pk):
    form_systemclass = get_object_or_404(SystemClass, pk=pk)

    return render(request, 'management/systemclass/systemclass_detail.html',
        {'form_systemclass': form_systemclass})


@login_required
def new_systemclass(request):
    if request.method == 'POST':
        formSystemClass = SystemClassForm(request.POST)
        if (formSystemClass.is_valid()):
            vsystemclass = formSystemClass.save(commit=False)
            vsystemclass.save()

            return redirect('/systemclass?op=success', {'systemclass':vsystemclass})
        else:
            return render(request, 'management/systemclass/systemclass_edit.html', {'form': formSystemClass})
    else:
        form = SystemClassForm()
        return render(request, 'management/systemclass/systemclass_edit.html', {'form': form})