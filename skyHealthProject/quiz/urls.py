from django.urls import path
from . import views
from core import views as core_views

urlpatterns = [
    path('', core_views.home_view, name='home'),
    path('quiz/<int:session_assignment_id>/', views.quiz_view, name='quiz'),
    path('complete/', views.quiz_success, name='complete'),
]