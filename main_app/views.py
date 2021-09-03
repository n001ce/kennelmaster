from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', { 'animals': animals })

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form':feeding_form })

class AnimalCreate(CreateView):
  model = Animal
  fields = ['type', 'breed', 'name', 'owner', 'description', 'age']

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['description', 'age', 'owner']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'