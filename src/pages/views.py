from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'index.html', {})


def scaler_app_view(request, *args, **kwargs):
    return render(request, 'scaler.html', {})


def input_chordData_view(request, *args, **kwargs):
    return render(request, 'input_chordData.html')
