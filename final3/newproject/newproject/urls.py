from django.contrib import admin
from django.urls import path, include  # Import include to include app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newapp.urls')),  # Include your app's URLs here
]
