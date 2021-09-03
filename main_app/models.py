from django.db import models
from django.urls import reverse

class Animal(models.Model):
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('animals_detail', kwargs={'animal_id':self.id})