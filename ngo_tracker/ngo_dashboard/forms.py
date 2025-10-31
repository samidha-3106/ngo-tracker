from django import forms
from .models import Project, NGOProfile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['ngo', 'title', 'description', 'status', 'start_date', 'end_date']

class NGOProfileForm(forms.ModelForm):
    class Meta:
        model = NGOProfile
        fields = ['name', 'description', 'address', 'contact']
