from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('publicar')

class Publicar(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    cuerpo = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")

    def __str__(self):
        return str(self.autor)

    def get_absolute_url (self):
        return reverse('publicar')
