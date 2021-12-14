from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('index',views.fun6,name='index'),
    path('student',views.fun2,name='student'),
    path('staff',views.fun3,name='staff'),
    path('home',views.fun4,name='home'),
    path('base',views.fun5,name='base'),
    path('dashboard',views.fun1,name='dashboard'),
    path('changepassword',views.fun7,name='changepassword'),
    path('editprofile',views.fun8,name='editprofile')
]