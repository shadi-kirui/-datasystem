from django.urls import path
from . import views

urlpatterns = [
     # Registration page
    
    path('dashboard', views.dashboard, name='dashboard'),  # Dashboard page
    path('',views.loginuser,name='login'),
    path('register',views.registeruser,name='register'),
    path('logout',views.logoutuser,name='logout'),
]
