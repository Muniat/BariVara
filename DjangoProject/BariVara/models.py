from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class advertisements(models.Model):
    place=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    bedroom=models.PositiveSmallIntegerField()
    bathroom=models.PositiveSmallIntegerField()
    rent=models.PositiveIntegerField()
    size=models.PositiveIntegerField()
    date_posted=models.DateTimeField(default=timezone.now)
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField()
    #images and google location will be added later


