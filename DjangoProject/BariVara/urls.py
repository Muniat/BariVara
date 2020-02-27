
from django.contrib import admin
from django.urls import path
from .views import (AdvertisementListView,
AdvertisementDetailsView,
AdvertisementCreateView,
AdvertisementUpdateView,
AdvertisementDeleteView)
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', AdvertisementListView.as_view(), name='HomePage'),
    path('advertisements/<int:pk>/',AdvertisementDetailsView.as_view() , name='advertisement_details'),
    path('create_advertisements',AdvertisementCreateView.as_view(), name='create_advertisements'),
    path('your_advertisements',views.your_advertisements, name='your_advertisements'),
    path('advertisements/<int:pk>/update',AdvertisementUpdateView.as_view() , name='advertisement_update'),
    path('advertisements/<int:pk>/delete',AdvertisementDeleteView.as_view() , name='advertisement_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
