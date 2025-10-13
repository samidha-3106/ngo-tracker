from django.contrib import admin
from django.urls import path, include  # include lets us connect app URLs

urlpatterns = [
    path('admin/', admin.site.urls),     # default admin page
    path('', include('ngo_app.urls')),  # this connects your app’s URLs
]