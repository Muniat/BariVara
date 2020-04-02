from django import forms
from . import models
from .models import Comment
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


	content = forms.CharField(label="" , widget = forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'text goes here' , 'rows':'4' , 'cols': '50'}))

	class Meta:

		model = Comment
		fields = ('content',)

       


     