from django import forms
from . import models
from django.forms import ModelForm

class advertisementForm(forms.ModelForm):
    class Meta:
        model= models.advertisements
        fields=['place','address','bedroom','bathroom','rent','size','number',]