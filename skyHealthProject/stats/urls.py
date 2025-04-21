from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats),
    path('engineer', views.engStats),
    path('team', views.teamStats),
    path('department', views.deptStats)
]