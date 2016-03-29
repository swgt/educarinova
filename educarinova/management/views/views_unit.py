from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from educarinova.management.models import Unit
from educarinova.management.forms.forms_units import UnitForm

@login_required
def list_unit(request):
    units = Unit.objects.all()
    return render(request, 'management/units/units_list.html', {'units': units})

@login_required
def new_unit(request):
    form = UnitForm()
    return render(request, 'management/units/units_edit.html', {'form': form})