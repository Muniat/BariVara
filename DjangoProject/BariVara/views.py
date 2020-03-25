from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import advertisements, Images
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)
from .import forms
from .forms import create_advertisements
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.forms import modelformset_factory
# Create your views here.

def HomePage(request):

    

    advertisements = advertisements.object.all()
    
    
    context={
        'advertisements': advertisements,
    }

    return render (request, 'BariVara/HomePage.html',context)

def Filter(request):

    query = request.GET['query']
    if query=="0":
        posts = advertisements.objects.filter(rent__gte=0)
        params = {'advertisements':posts}
        return render(request, 'BariVara/filter.html', params)
    elif query=="1":
        posts = advertisements.objects.filter(rent__lt=15000)
        params = {'advertisements':posts}
        return render(request, 'BariVara/filter.html', params)
    elif query=="2":
        posts = advertisements.objects.filter(rent__range=(15000,20000))
        params = {'advertisements':posts}
        return render(request, 'BariVara/filter.html', params)
    elif query=="3":
        posts = advertisements.objects.filter(rent__range=(20001,25000))
        params = {'advertisements':posts}
        return render(request, 'BariVara/filter.html', params)
    elif query=="4":
        posts = advertisements.objects.filter(rent__range=(25001,30000))
        params = {'advertisements':posts}
        return render(request, 'BariVara/filter.html', params)
    elif query=="5":
        posts = advertisements.objects.filter(rent__gt=30000)
        params = {'advertisements':posts}
        return render(request, 'BariVara/filter.html', params)    
        
    

def Search(request):

    query = request.GET['query']
    posts = advertisements.objects.filter(place__icontains=query)
    params = {'advertisements':posts}
    return render(request, 'BariVara/search.html', params)


def your_advertisements(request):
    advertisement={
        'advertisements': advertisements.objects.all()
    }
    return render (request, 'BariVara/your_advertisements.html',advertisement)

class AdvertisementDetailsView(DetailView):
    model=advertisements
    template_name= 'BariVara/advertisement_details.html'
#def advertisement_detail(request):
    #advertisement = get_object_or_404(advertisements, id=id)
    #context={
      #'advertisement' : advertisement
    #}
    #return render(request, 'BariVara/advertisement_details.html', context)


#class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    #model= advertisements
    #fields=['image','place','address','bedroom','bathroom','rent','size','number']
def create_advertisement(request):

    ImageFormset = modelformset_factory(Images, fields=('image',), extra=4)
    if request.method == 'POST':
        form = create_advertisements(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            advertisement = form.save(commit=False)
            advertisement.owner = request.user
            advertisement.save()

            for f in formset:
                try:
                    photo = Images(image=f.cleaned_data['image'])
                    photo.save()

                except Exception as e:
                    break
    else:
        form = create_advertisements()
        formset = ImageFormset(queryset=advertisements.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'BariVara/create_advertisements.html', context)



    #def form_valid(self, form):
        #form.instance.owner=self.request.user
        #return super().form_valid(form)

class AdvertisementUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= advertisements
    fields=['image','place','address','bedroom','bathroom','rent','size','number']

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        advertisements= self.get_object()
        if self.request.user == advertisements.owner:
            return True
        return False

class AdvertisementDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model= advertisements
    success_url = reverse_lazy('your_advertisements') 
    def test_func(self):
        advertisements= self.get_object()
        if self.request.user == advertisements.owner:
            return True
        return False

class AdvertisementListView(ListView):
    model = advertisements
    template_name = 'BariVara/Homepage.html'
    context_object_name = 'advertisements'
    ordering = ['-date_posted']



    
