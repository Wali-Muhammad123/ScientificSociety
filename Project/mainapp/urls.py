from django.urls import path
from . import views
app_name='mainapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('profile/edit/password/',views.edit_password,name='edit_password'),
    path('profile/edit/society/',views.edit_society,name='edit_society'),
    path('profile/edit/level/',views.edit_level,name='edit_level'),
    path('profile/edit/name/',views.edit_name,name='edit_name'),
    path('joinsociety/',views.join_society,name='join_society'),
    path('gallery/',views.gallery,name='gallery'),
]