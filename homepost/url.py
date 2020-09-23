from django.contrib import admin

from django.urls import path

from homepost import views

urlpatterns = [
    
    path('',views.home_post , name = 'homepost'),
    
    path('addpost/',views.add_post, name = 'addpost'),
    path('addpost/succes/', views.add_post_succes),
    
    path('deletepost/',views.delete_post),
    
    path('updatepost/',views.update_post),
    path('deletepost/updated/',views.update_post_updated),
    
    path('selectpost/',views.select_post , name = 'selectpost'),
    
    path('logout/',views.logout, name = 'logout')
 
]