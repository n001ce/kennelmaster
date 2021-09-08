from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .models import Animal, Task, NewUser
from .forms import FeedingForm, TaskForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', { 'animals': animals })


def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form':feeding_form})

def user_animal(request, user_id):
  animal = Animal.objects.filter(user=user_id)
  return render(request, 'animals/detail.html', {'animal': animal})

def profiles_detail(request, user_id):
  user = NewUser.objects.get(id=user_id)
  task_form = TaskForm()
  return render(request, 'profiles/detail.html', { 'user': user, 'task_form':task_form })


def add_feeding(request, animal_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.animal_id = animal_id
        new_feeding.save()
    return redirect('animals_detail', animal_id=animal_id)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class AnimalCreate(CreateView):
  model = Animal
  fields = ['type', 'breed', 'name', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['description', 'age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'

class TaskCreate(CreateView):
  model = Task
  fields = '__all__'

class TaskList(ListView):
  model = Task

class TaskDetail(DetailView):
  model = Task

class TaskUpdate(UpdateView):
  model = Task
  fields = ['start_time', 'end_time', 'type','description']

class TaskDelete(DeleteView):
  model = Task
  success_url = '/tasks/'

def assoc_task(request, employee_id, task_id):
  Employee.objects.get(id=employee_id).Tasks.add(task_id)
  return redirect('employees_detail', employee_id=employee_id)
