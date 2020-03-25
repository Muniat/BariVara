from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import advertisements,images
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
def HomePage(request):
    
    context={
        'advertisements':advertisements.objects.all()
    }
    return render (request, 'BariVara/HomePage.html',context)


def create_advertisements(request):
    ImageFormset= modelformset_factory(images,fields=('image',),extra=3)
    if request.method=='POST':
        form=advertisementForm(request.POST)
        formset=ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            advertisement=form.save(commit=False)
            advertisement.owner=request.user
            advertisement.save()
            for f in formset:
                try:
                    photo=images(advertisement=advertisement,image=f.cleaned_data['image'])
                    photo.save()
                    
                except Exception as e:
                    break
            return redirect('HomePage')
            
    else:
        form=advertisementForm()
        formset= ImageFormset(queryset=images.objects.none())
    
    context={
        'form':form,
        'formset':formset,
    }
    return render (request,'BariVara/create_advertisements.html',context)

def advertisement_edit(request, id):
    advertisement = get_object_or_404(advertisements, id=id)
    if advertisement.owner != request.user:
        raise Http404()
    if request.method == "POST":
        form = advertisementEditForm(request.POST or None, instance=advertisement)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(advertisement.get_absolute_url())
    else:
        form = advertisementEditForm(instance=advertisement)
        context = {
            'form': form,
            'advertisement': advertisement,
        }
    return render(request, 'Barivara/advertisement_edit.html', context)

def advertisement_delete(request, id):
    advertisement = get_object_or_404(advertisements, id=id)
    if advertisement.owner != request.user:
        raise Http404()
    advertisement.delete()
    return redirect('HomePage')
        
def your_advertisements(request):
    advertisement={
        'advertisements': advertisements.objects.all()
    }
    return render (request, 'BariVara/your_advertisements.html',advertisement)

def advertisement_details(request,id):
    context={
        'advertisement':advertisements.objects.get(id=id)
    }
    
    return render(request,'BariVara/advertisement_details.html',context)

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


