"""Barivara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signIn),
    path('postsign', views.postsign, name="home"),
    path('welcome', views.postgooglelogin, name="welcome"),
    path('api/v1/',include('social_django.urls', namespace='social')),
    path('logout', views.logout, name="log"),
    path('postsignup', views.postsignup, name="postsignup"),
    path('create_advertisement', views.create_advertisement, name="create_advertisement"),
    path('create', views.create, name="create"),
	path('your_advertisements', views.your_advertisements, name="your_advertisements"),
    path('advertisement_details/', views.advertisement_details, name="advertisement_details"),
    path('edit_advertisement/', views.edit_advertisement, name="edit_advertisement"),
]

