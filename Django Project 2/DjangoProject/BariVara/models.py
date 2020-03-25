from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class advertisements(models.Model):
    PLACE=[
        ('mothijheel', 'Mothijheel'),
        ('bonosree', 'Bonosree'),
        ('mirpur', 'Mirpur'),
        ('khilgao', 'Khilgao'),
        ('gulshan', 'Gulshan'),
        ('badda', 'Badda'),
        ('uttora', 'Uttora'),
        ('banani', 'Banani'),
    ]
    place=models.CharField(max_length=30,choices=PLACE)
    address=models.CharField(max_length=50)
    bedroom=models.PositiveSmallIntegerField()
    bathroom=models.PositiveSmallIntegerField()
    rent=models.PositiveIntegerField()
    size=models.PositiveIntegerField()
    date_posted=models.DateTimeField(default=timezone.now)
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    number=models.PositiveIntegerField(null=True)
    

    
    # google location will be added later

    def get_absolute_url(self):
        return reverse('advertisement_details', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class images(models.Model):
    advertisement=models.ForeignKey(advertisements,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='house_pics/',blank=True, null=True)

    def __str__(self):
        return self.advertisements.place + "Image"

    
    
