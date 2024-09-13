from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from .models import EwasteCenters
from geopy.distance import geodesic
from django.http import JsonResponse

# Home page
def index(request):
    return render(request, 'index.html')

# Signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout page
def user_logout(request):
    logout(request)
    return redirect('login')

# Services page
def services(request):
    username = request.user.username

    centers = list(EwasteCenters.objects.values('latitude', 'longitude'))
    context = {'username': username, 'centers': centers}
    return render(request, 'services.html', context)

# About page
def about(request):
    return render(request, 'about.html')

def nearest_center(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    user_location = latitude, longitude
    center_distances = {}
    for center in EwasteCenters.objects.all()[:100]:
        center_location = center.latitude, center.longitude
        distance = geodesic(user_location, center_location).kilometers
        center_distances[distance] = center_location

    min_distance = min(center_distances)
    center_coords = center_distances[min_distance]

    return JsonResponse({
        'coordinates': center_coords,
        'distance': min_distance
    })

