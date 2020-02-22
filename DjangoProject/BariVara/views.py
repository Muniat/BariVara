from django.shortcuts import render
from django.http import HttpResponse
from .models import advertisements
from django.views.generic import ListView

# Create your views here.
'''
def LoginPage(request):
    return render (request,'BariVara/LoginPage.html')'''
def HomePage(request):
    context = {
        'advertisements' : advertisements.objects.all()
    }
    return render (request, 'BariVara/HomePage.html', context)

class AdvertisementListView(ListView):
    model = advertisements
    template_name = 'BariVara/Homepage.html'
    context_object_name = 'advertisements'
    ordering = ['-date_posted']