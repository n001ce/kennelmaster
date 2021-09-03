from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import FeedingForm, OwnerForm

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

def add_feeding(request, animal_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.animal_id = animal_id
        new_feeding.save()
    return redirect('animals_detail', animal_id=animal_id)

def add_owner(request, animal_id):
    form = OwnerForm(request.POST)
    if form.is_valid():
        new_owner = form.save(commit=False)
        new_owner.animal_id = animal_id
        new_owner.save()
    return redirect('animals_detail', animal_id=animal_id)

class AnimalCreate(CreateView):
  model = Animal
  fields = ['type', 'breed', 'name', 'owner', 'description', 'age']

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['description', 'age', 'owner']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'