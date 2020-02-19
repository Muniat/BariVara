from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserSignUpForm

def signup(request):
    if request.method =='POST':
        form=UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form=UserSignUpForm()
    return render(request, 'users/signup.html',{'form':form})

def HomePage(request):
    return render(request, 'users/Login.html')

