
from django.contrib import admin
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.HomePage, name='HomePage'),
    path('create_advertisements', views.create_advertisements, name='create_advertisements'),
    path('advertisement_details/<int:id>/', views.advertisement_details, name='advertisement_details'),
    path('search', views.Search, name='search'),
    path('filter', views.Filter, name='filter'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
