from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ngo_dashboard/', include('ngo_dashboard.urls')),  # <-- this line
]
