from django.contrib import admin
from django.urls import path, include
from ngo_app import views  # import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ngo_app.urls')),  
    path('users/', include('users.urls')),
    
]
