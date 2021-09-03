from django.contrib import admin
# import your models here
from .models import Animal, Feeding

# Register your models here
admin.site.register(Animal)
admin.site.register(Feeding)