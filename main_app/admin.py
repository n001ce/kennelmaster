from django.contrib import admin
# import your models here
from .models import Animal, Feeding, Owner, Task, Employee

# Register your models here
admin.site.register(Animal)
admin.site.register(Feeding)
admin.site.register(Owner)
admin.site.register(Task)
admin.site.register(Employee)