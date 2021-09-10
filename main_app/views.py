from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .models import Animal, Task, NewUser, Employee, Photo
from .forms import FeedingForm, TaskForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'kennel-manager'

class Login(LoginView):
  template_name = 'login.html'

@login_required
def home(request):
  tasks = Task.objects.all()
  animals = Animal.objects.all()
  employees = Employee.objects.all()
  return render(request, 'home.html', {'tasks':tasks, 'employees':employees, 'animals':animals})

def about(request):
    return render(request, 'about.html')

@login_required
def animals_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', { 'animals': animals })

@login_required
def profiles_index(request):
    profiles = NewUser.objects.all()
    return render(request, 'profiles/index.html', { 'profiles': profiles })

@login_required
def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form':feeding_form})

@login_required
def user_animal(request, user_id):
  animal = Animal.objects.filter(user_id=user_id)
  return render(request, 'animals/detail.html', {'animal': animal})

@login_required
def profiles_detail(request, user_id):
  user = NewUser.objects.get(id=user_id)
  tasks = Task.objects.filter(employee_id = user_id)
  return render(request, 'profiles/detail.html', { 'user': user, 'tasks':tasks })

@login_required
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


class NewUserUpdate(UpdateView):
  model = NewUser
  fields = ['first_name', 'email']


class NewUserDelete(DeleteView):
  model = NewUser
  success_url = '/home'


class TaskCreate(CreateView):
  model = Task
  fields = '__all__'


class TaskList(ListView):
  model = Task


class TaskDetail(DetailView):
  model = Task


class TaskUpdate(UpdateView):
  model = Task
  fields = ['start_time', 'end_time', 'type','description', 'is_complete']


class TaskDelete(DeleteView):
  model = Task
  success_url = '/tasks/'

@login_required
def add_photo(request, animal_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, animal_id=animal_id)
      animal_photo = Photo.objects.filter(animal_id=animal_id)
      if animal_photo.first():
        animal_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('animals_detail', animal_id=animal_id)

