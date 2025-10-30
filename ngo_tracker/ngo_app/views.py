from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse("Welcome to the NGO Tracker Website 🌍")

@login_required
def profile(request):
    return render(request, 'profile.html')  # make sure to create this template

 


