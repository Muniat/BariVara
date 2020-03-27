from django import forms
from . import models
from django.forms import ModelForm

class advertisementForm(forms.ModelForm):
    class Meta:
        model= models.advertisements
        fields=['place','address','bedroom','bathroom','rent','size','number',]

class advertisementEditForm(forms.ModelForm):
    class Meta:
        model= models.advertisements
        fields=['place','address','bedroom','bathroom','rent','size','number',]        


class commentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['content',]