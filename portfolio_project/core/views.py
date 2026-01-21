from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required # Protects pages
from .forms import RegisterForm # Import the form we just made
from django.shortcuts import render, redirect # Ensure redirect is imported

# In core/views.py

from django.shortcuts import render
# from django.http import HttpResponse # Not needed when using 'render'

# View for the Home Page
def home(request):
    # This renders an HTML template named 'home.html'
    return render(request, 'home.html')

# View for the About Page
def about(request):
    return render(request, 'about.html')

# View for the Contact Page
def contact(request):
    return render(request, 'contact.html')

# 1. REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Saves the user to DB
            login(request, user) # Auto-login after registration
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# 2. LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() # Get the user object from the form
            login(request, user) # Starts the session
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. LOGOUT VIEW
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

# 4. DASHBOARD (Protected Page)
@login_required(login_url='login') # Redirects to login if not signed in
def dashboard(request):
    return render(request, 'dashboard.html')
