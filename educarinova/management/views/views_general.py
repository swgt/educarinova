from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def register(request):
    return render(request, 'registration/register.html')


@login_required
def dashboard(request):
    return render(request, 'management/dashboard.html')