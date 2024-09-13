from django.urls import path
from newapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get-nearest-center/', views.nearest_center, name='get_nearest_center'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('services/', views.services, name='services'), 
    path('about/', views.about, name='about'),  
    #path('adddata/',views.data)

]