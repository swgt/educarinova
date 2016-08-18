from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from educarinova.management.models import Class, Matriculation, SystemClass, ClassSystemClass
from educarinova.management.forms.forms_class import ClassForm
from pprint import pprint


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

    return render(request, 'management/class/class_detail.html', 
        {'form_class': form_class, 'matriculations': matriculations})


@login_required
def new_class(request):

    list_selected_systems = []

    if request.method == 'POST':
        formClass = ClassForm(request.POST)

        obj_systems = {
            'id': '',
            'valueTuitionFee': '',
            'vacancies': '',
            'message':'' 
        }

        
        check = False

        for param in request.POST:
            if "_name_check" in param:
                idSystemClass = request.POST.get(param)
                valueTuitionFee = request.POST.get(idSystemClass+"_name_mensalidade")
                vacancies = request.POST.get(idSystemClass+"_name_vagas")

                obj_systems['id'] = idSystemClass
                obj_systems['valueTuitionFee'] = valueTuitionFee
                obj_systems['vacancies'] = vacancies
                obj_systems['message'] = ''

                check = True

                if not(valueTuitionFee and vacancies):
                    obj_systems['message'] = 'Preencha os dois campos abaixo!'
                    check = False

                list_selected_systems.append(obj_systems)

                obj_systems = {
                    'id': '',
                    'valueTuitionFee': '',
                    'vacancies': '',
                    'message':'' 
                }

        if (formClass.is_valid()):
            vclass = formClass.save(commit=False)

            vclass.save()

            if (check):
                for sc in list_selected_systems:
                    systemClass = SystemClass.objects.get(pk=sc['id'])
                    classSystemClass = ClassSystemClass()

                    classSystemClass.classv = vclass
                    classSystemClass.system_class = systemClass
                    classSystemClass.value_tuition_fee = sc['valueTuitionFee']
                    classSystemClass.vacancies = sc['vacancies']

                    classSystemClass.save()
            else:
                vclass.delete()
                print (list_selected_systems)
                systems = SystemClass.objects.all()
                return render(request, 'management/class/class_edit.html', {'form': formClass, 'systems':systems, 'list_selected_systems':list_selected_systems})

            return redirect('/class?op=success', {'class':vclass})
        else:
            systems = SystemClass.objects.all()
            return render(request, 'management/class/class_edit.html', {'form': formClass, 'systems':systems, 'list_selected_systems':list_selected_systems})
    else:
        form = ClassForm()
        systems = SystemClass.objects.all()
        return render(request, 'management/class/class_edit.html', {'form': form, 'systems':systems,
            'list_selected_systems':list_selected_systems})