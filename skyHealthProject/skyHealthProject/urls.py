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
from core.views import logout_view
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from user import views as user_views
#Line 26 by Muhammad Ravat (w1984454) - Imported stats.urls folder so I can handle my routes in my app. 
# Lines 28-43 were done by Iqra Shah (w1973224)
#Line 53 was implemented by Mohi (1972510)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/', include('stats.urls')),
    path('captcha/', include('captcha.urls')),

    # Auth
    path('signup/', core_views.signup_view, name='signup'),
    path('login/', core_views.login_view, name='login'),

    # Email Verification and Account Activation
    path('activate/<uidb64>/<token>/', core_views.activate_account, name='activate_account'),
    path('email_verification/', core_views.email_verification, name='email_verification'),

    # Home + Dashboards 
    path('', core_views.home_view, name='home'),
    path("deptLead/", user_views.d_lead_dashboard_view, name="d_lead_dashboard"),
    path("engineer/", user_views.engineer_dashboard_view, name="engineer_dashboard"),
    path("senior/", user_views.senior_dashboard_view, name="senior_dashboard"),
    path("teamLead/", user_views.team_lead_dashboard_view, name="team_lead_dashboard"),

    # Profile 
    path('profile/', user_views.profile_view, name='profile'),

    # Quiz 
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('stats/', include('stats.urls')), 

    path('logout/', logout_view, name='logout'),
]
