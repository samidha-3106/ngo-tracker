from django import forms
from .models import Project, NGOProfile

# Form for adding/editing a Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['ngo', 'title', 'description', 'status', 'start_date', 'end_date']

# Optional: Form for NGO Profile (if you want to add/edit NGOs later)
class NGOProfileForm(forms.ModelForm):
    class Meta:
        model = NGOProfile
        fields = ['name', 'description', 'address', 'contact']
