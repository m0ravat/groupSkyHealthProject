from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadStats),
    path('engineer', views.engStats),
    path('team', views.teamStats),
    path('department', views.deptStats)
]