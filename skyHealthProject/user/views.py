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