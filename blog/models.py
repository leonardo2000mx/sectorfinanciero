from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Publicar(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    cuerpo = models.TextField()
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.autor)

    def get_absolute_url (self):
        return reverse('publicar')
