from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
#def profile_view(request):
    #user = request.user 

def profile_view(request):
    return render(request, 'profile.html') 
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form})

# Views for different dashboards based on role
def d_lead_dashboard_view(request):
    return render(request, "dLeadDashboard.html")

def engineer_dashboard_view(request):
    return render(request, "engineerDashboard.html")

def senior_dashboard_view(request):
    return render(request, "seniorDashboard.html")

def team_lead_dashboard_view(request):
    return render(request, "teamLead_dashboard.html")