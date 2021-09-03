from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def animals_index(request):
  return render(request, 'animals/index.html', { 'animals': animals })

class Animal :
    def __init__(self, type, name, breed, age, owner, description):
        self.type=type
        self.name=name
        self.breed=breed
        self.age=age
        self.owner=owner
        self.description=description
animals=[
    Animal('Snake', 'Bali', 'Python', 3, 'Jessica Schmidt', 'Im a slithery snake'),
    Animal('Dog', 'Ruffus', 'Lab', 5, 'Allan Might', 'Im a good boy'),
    Animal('Cat', 'Precious', 'American Bobtail', 3, 'Steven Tai', 'Diva'),
    Animal('Rabbit', 'Hoppy', 'Netherland Dwarf', 3, 'Michelle Olama', 'They are a real jumper'),
    ]