from django.urls import path
from . import views
app_name='mainapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('joinsociety/',views.join_society,name='join_society'),
    path('gallery/',views.gallery,name='gallery'),
]