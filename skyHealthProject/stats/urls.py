# All code by Muhammad ravat (w1984454)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadStats, name='stats'),
    path('engineer', views.engStats),
    path('team', views.teamStats),
    path('department', views.deptStats)
]