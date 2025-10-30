from django.shortcuts import render
from django.contrib.auth.models import User
from ngo_dashboard.models import NGOProfile, Project

def home(request):
    context = {
        'total_ngos': NGOProfile.objects.count(),
        'total_projects': Project.objects.count(),
        'total_users': User.objects.count(),
    }
    return render(request, 'home.html', context)

def ngo_list(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        # Search in both name and description
        ngos = NGOProfile.objects.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(address__icontains=search_query)
        )
    else:
        ngos = NGOProfile.objects.all()
    
    context = {
        'ngos': ngos,
        'search_query': search_query,
        'total_results': ngos.count()
    }
    return render(request, 'ngo_app/ngo_list.html', context)

def ngo_detail(request, ngo_id):
    ngo = get_object_or_404(NGOProfile, id=ngo_id)
    projects = Project.objects.filter(ngo=ngo)
    
    context = {
        'ngo': ngo,
        'projects': projects,
        'total_projects': projects.count()
    }
    return render(request, 'ngo_app/ngo_detail.html', context)