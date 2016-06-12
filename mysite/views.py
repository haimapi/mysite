__author__ = 'Administrator'
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')