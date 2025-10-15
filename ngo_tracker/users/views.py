from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import UserProfile

# Signup View
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # create user
            user = User.objects.create_user(username=username, password=password)
            
            # link with user profile
            UserProfile.objects.create(user=user, role=role)

            return redirect('login')  # after signup, go to login page
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to home after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
