from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from educarinova.management.models import Serie
from educarinova.management.forms.forms_series import SerieForm

@login_required
def list_serie(request):
    series = Serie.objects.all().order_by('-id')
    return render(request, 'management/serie/serie_list.html', {'series': series})

@login_required
def new_serie(request):

	if request.method == 'POST':
		formSerie = SerieForm(request.POST)
		if (formSerie.is_valid()):
			serie = formSerie.save(commit=False)
			serie.save()

			return redirect('/serie?op=success', pk='teste')
		else:
			return render(request, 'management/serie/serie_edit.html', {'form': formSerie})
	else:
		form = SerieForm()
		return render(request, 'management/serie/serie_edit.html', {'form': form})