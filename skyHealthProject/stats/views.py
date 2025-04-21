from django.shortcuts import render
from django.http import HttpResponse
from templates import *
# Create your views here.

def stats(request): 
    return render(request, 'statsPage.html')

def engStats(request):
    return render(request, 'engStats.html')

def teamStats(request):
    return render(request, 'teamStats.html')

def deptStats(request):
    return render(request, 'deptStats.html')