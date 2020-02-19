from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def LoginPage(request):
    return render (request,'BariVara/LoginPage.html')
def HomePage(request):
    return render (request, 'BariVara/HomePage.html')

