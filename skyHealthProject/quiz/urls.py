from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page: select/create session
    path('quiz/<int:session_assignment_id>/', views.quiz, name='quiz'),  # Quiz page for session
    path('complete/', views.complete, name='complete'),  # Quiz completed page
]