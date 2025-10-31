from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import NGOProfile, Project
from .forms import ProjectForm, NGOProfileForm  # we'll create these forms next

# NGO Dashboard Home
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'ngo_dashboard/dashboard.html', {'projects': projects})

# Add new project
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'ngo_dashboard/add_project.html', {'form': form})

# Edit project
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'ngo_dashboard/edit_project.html', {'form': form})

# Delete project
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('dashboard')

# Create your views here.
