from django.urls import path
from . import views
from core import views as core_views

urlpatterns = [
    path('', core_views.home_view, name='quiz'),  # Home view from 'core' app
    path('quiz/', views.quiz_view, name='quiz1'),  # Fixed: removed parameter
    path('complete/', views.quiz_success, name='complete'),
]
