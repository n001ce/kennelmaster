from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import date, time
MEALS = (
    ('B', 'Breakfast'),
    ('D', 'Dinner')
)

TASKS = (
    ('K', 'Kennel Cleaning'),
    ('G', 'Group Play'),
    ('M', 'Medications'),
    ('F', 'Feeding'),
)



class Animal(models.Model):
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('animals_detail', kwargs={'animal_id':self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
   
    def has_owner(self):
        return self.owner_set.count() >= 1
    
    def located_at(self):
        return self.room_set.count()>=1

class Room(models.Model):
    room = models.IntegerField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    is_clean = models.BooleanField()

    def __str__(self):
        return self.room
    
    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'room_id':self.id})
    

class Employee(models.Model):
    s_date = models.DateField('Employment Start')
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    p_num = models.IntegerField()
    emergency_contact = models.TextField(max_length=200)

    def __str__(self):
        return self.f_name
    
    def get_absolute_url(self):
        return reverse('employees_detail', kwargs={'employee_id':self.id})
    
    def has_task(self):
        return self.task_set.count() >= 1


class Owner(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    p_num = models.IntegerField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Owner for animal_id: {self.animal_id}"


class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default=MEALS[0][0]
        )
    food = models.CharField(max_length=50)
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Task(models.Model):
    start_time = models.TimeField('Task Start')
    end_time = models.TimeField('Task End')
    type = models.CharField(
        max_length=1,
        choices= TASKS,
        default=TASKS[0][0]
    )
    description = models.TextField(max_length=250)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)

    def __str__(self):
        return self.type
        
    def get_absolute_url(self):
        return reverse("tasks_detail", kwargs={"pk": self.id})
