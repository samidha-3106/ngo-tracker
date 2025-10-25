from django.contrib import admin
from .models import NGOProfile, Project

@admin.register(NGOProfile)
class NGOProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address')
    search_fields = ('name', 'contact')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'ngo', 'status', 'start_date', 'end_date')
    search_fields = ('title', 'ngo__name')
    list_filter = ('status', 'start_date')