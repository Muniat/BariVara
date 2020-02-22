
from django.contrib import admin
from django.urls import path
from .views import AdvertisementListView
from . import views

urlpatterns = [
    
    path('', AdvertisementListView.as_view(), name='HomePage'),
    path('create_advertisements',views.create_advertisements, name='create_advertisements'),
]