from django.contrib import admin
# import your models here
from .models import Animal, Feeding, Owner

# Register your models here
admin.site.register(Animal)
admin.site.register(Feeding)
admin.site.register(Owner)