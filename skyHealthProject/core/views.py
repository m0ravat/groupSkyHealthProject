from django.shortcuts import render

# Iqra Shah (w1973224)
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def dashboard(request):
    return render(request, "dashboard.html", {"user": request.user})
