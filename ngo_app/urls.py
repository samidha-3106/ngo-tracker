from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ngos/', views.ngo_list, name='ngo_list'),
    path('ngo/<int:ngo_id>/', views.ngo_detail, name='ngo_detail'),
         
]