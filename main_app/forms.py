from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Feeding, Task, NewUser

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['start_time', 'end_time', 'type', 'description']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ('type', 'email', 'user_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = NewUser
        fields = ('email', 'user_name')