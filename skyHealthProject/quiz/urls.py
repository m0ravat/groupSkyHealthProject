#This file was coded by Barket Omar Sheikh (w2045831) and Iqra Shah corrected it to fix paths (w1973224)

from django.urls import path
from . import views
from core import views as core_views

urlpatterns = [
    path('', core_views.home_view, name='quiz'),  
    path('quiz/', views.quiz_view, name='quiz1'),  
    path('complete/', views.quiz_success, name='complete'),
]
