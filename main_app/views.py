from django.shortcuts import render
from .models import Animal

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', { 'animals': animals })

