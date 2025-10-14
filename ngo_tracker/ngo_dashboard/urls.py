from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),           # NGO Dashboard Home
    path('add/', views.add_project, name='add_project'),   # Add new project
    path('edit/<int:pk>/', views.edit_project, name='edit_project'),  # Edit project
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),  # Delete project
]

