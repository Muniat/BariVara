
from django.contrib import admin
from django.urls import path
from .views import AdvertisementListView,AdvertisementDetailsView
from . import views

urlpatterns = [
    
    path('', views.HomePage, name='HomePage'),
    path('advertisements/<int:pk>/',AdvertisementDetailsView.as_view() , name='advertisement_details'),
    path('create_advertisements',views.create_advertisements, name='create_advertisements'),
    path('your_advertisements',views.your_advertisements, name='your_advertisements'),
]