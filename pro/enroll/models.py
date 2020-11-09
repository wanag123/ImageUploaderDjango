from django.db import models
from django.urls import reverse

class Image(models.Model):
    photo  = models.ImageField(upload_to='myimages')
    uploaded =  models.DateField(auto_now_add=True)
    