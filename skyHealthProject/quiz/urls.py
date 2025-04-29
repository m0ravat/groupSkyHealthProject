# This file was coded by Barket Omar Sheikh (w2045831) and Iqra Shah corrected it to fix paths (w1973224)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),      # /quiz/
    path('complete/', views.quiz_success, name='complete'),  # /quiz/complete/
]
