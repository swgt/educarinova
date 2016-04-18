from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from educarinova.management.models import Unit
from educarinova.management.forms.forms_units import UnitForm
from educarinova.management.forms.forms_address import AddressForm
from educarinova.management.forms.forms_contact import ContactForm

@login_required
def list_unit(request):
    units = Unit.objects.all()
    return render(request, 'management/units/units_list.html', {'units': units})

@login_required
def new_unit(request):


	if request.method == 'POST':

		unitForm = UnitForm(request.POST)
		addressForm = AddressForm(request.POST)
		contactForm = ContactForm(request.POST)

		if (unitForm.is_valid() and addressForm.is_valid() and contactForm.is_valid()):
			address = addressForm.save(commit=False)
			address.save()

			contact = contactForm.save(commit=False)
			contact.save()

			unit = unitForm.save(commit=False)
			unit.address = address
			unit.contact = contact

			unit.save()

			return redirect('/unit?op=success')
		else:
			return render(request, 'management/units/units_edit.html', {'unitForm': unitForm, 'addressForm': addressForm, 'contactForm':contactForm})
	else:
		unitForm = UnitForm()
		addressForm = AddressForm()
		contactForm = ContactForm()

		return render(request, 'management/units/units_edit.html', {'unitForm': unitForm, 'addressForm': addressForm, 'contactForm':contactForm})


