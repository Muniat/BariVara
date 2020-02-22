from django import forms
from . import models

class create_advertisements(forms.ModelForm):
    class Meta:
        model= models.advertisements
        fields=['place','address','bedroom','bathroom','rent','size']