# All code by Muhammad ravat (w1984454)

from django.shortcuts import render
from templates import *
# Create your views here.

def loadStats(request): 
    return render(request, 'statsPage.html')

def engStats(request):
    return render(request, 'engStats.html')

def teamStats(request):
    return render(request, 'teamStats.html')

def deptStats(request):
    return render(request, 'deptStats.html')