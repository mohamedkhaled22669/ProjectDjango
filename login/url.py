from django.contrib import admin

from django.urls import path
from django.views.generic import TemplateView
from login import views

urlpatterns = [
    
    # path('register/', views.register, name = 'register'),
    path('register/',TemplateView.as_view(template_name = 'sign/register.html'),name = 'register'),
    path('register/accept/', views.register_accept),
    
    
    # path('login/',views.login, name = 'login'),
    path('login/',TemplateView.as_view(template_name = 'sign/login.html'),name = 'login'),
    path('login/accept/',views.login_accept),
    
    
    
    
    
    
]