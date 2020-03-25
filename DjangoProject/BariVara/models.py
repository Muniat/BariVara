from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

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
    number=models.PositiveIntegerField(null=True)
    #image = models.ImageField(default='defaulthouse.jpg',upload_to='house_pics/')


    
    # google location will be added later

    def get_absolute_url(self):
        return reverse('advertisement_details', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #image=Image.open(self.image.path)


class Images(models.Model):
    advertisement = models.ForeignKey(advertisements,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='house_pics/',blank=True,null=True)
    def __str__(self):
        return self.advertisement.place + 'Image'


