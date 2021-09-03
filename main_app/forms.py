from django.forms import ModelForm
from .models import Feeding, Owner

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class OwnerForm(ModelForm):
  class Meta:
    model = Owner
    fields = ['f_name', 'l_name', 'p_num']