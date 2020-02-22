from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import advertisements
from django.views.generic import ListView
from .import forms
from django.contrib import messages

# Create your views here.
'''
def LoginPage(request):
    return render (request,'BariVara/LoginPage.html')'''
def HomePage(request):
    context = {
        'advertisements' : advertisements.objects.all()
    }
    return render (request, 'BariVara/HomePage.html', context)

def create_advertisements(request):
    form=forms.create_advertisements()
    if request.method=='POST':
        form=forms.create_advertisements(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.owner= request.user
            instance.save()
            
            return HttpResponse ("Post Created") # need to fix this url
    else:
        form=forms.create_advertisements()

    return render (request,'BariVara/create_advertisements.html',{'form':form})

class AdvertisementListView(ListView):
    model = advertisements
    template_name = 'BariVara/Homepage.html'
    context_object_name = 'advertisements'
    ordering = ['-date_posted']