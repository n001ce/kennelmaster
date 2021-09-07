from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Feeding, Owner, Task, NewUser

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class OwnerForm(ModelForm):
  class Meta:
    model = Owner
    fields = ['f_name', 'l_name', 'p_num']

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['start_time', 'end_time', 'type', 'description']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ('email', 'user_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = NewUser
        fields = ('email', 'user_name')