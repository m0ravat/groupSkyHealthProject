"""
URL configuration for skyHealthProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from user import views as user_views

# Lines 26-40 were done by Iqra Shah (w1973224)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/', include('stats.urls')),
    path('captcha/', include('captcha.urls')),

    # Auth
    path('signup/', core_views.signup_view, name='signup'),
    path('login/', core_views.login_view, name='login'),

    # Home + Dashboards (core views)
    path('', core_views.home_view, name='home'),
    path("deptLead/", user_views.d_lead_dashboard_view, name="d_lead_dashboard"),
    path("engineer/", user_views.engineer_dashboard_view, name="engineer_dashboard"),
    path("senior/", user_views.senior_dashboard_view, name="senior_dashboard"),
    path("teamLead/", user_views.team_lead_dashboard_view, name="team_lead_dashboard"),

    # Profile (user view)
    path('profile/', user_views.profile_view, name='profile'),
]
