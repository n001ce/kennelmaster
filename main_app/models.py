from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import date, time
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    class Types(models.TextChoices):
        MANAGER = "MANAGER", "Manager"
        EMPLOYEE = "EMPLOYEE", "Employee"
        OWNER  = "OWNER", "Owner"
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.EMPLOYEE)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

class ManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.MANAGER)
class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.EMPLOYEE)
class OwnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.OWNER)


class Manager(NewUser):
    objects = ManagerManager()
    class Meta:
        proxy=True

class Employee(NewUser):
    objects = EmployeeManager()
    class Meta:
        proxy=True

class Owner(NewUser):
    objects=OwnerManager()
    class Meta:
        proxy=True

class Animal(models.Model):

    class Types(models.TextChoices):
        DOG = "DOG", "Dog"
        CAT = "CAT", "Cat"
        REPTILE  = "REPTILE", "Reptile"
        BIRD = "BIRD", "Bird"
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.DOG)
    breed = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(NewUser, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('animals_detail', kwargs={'animal_id':self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
       
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

class Photo(models.Model):
    url = models.CharField(max_length=250)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for {self.id}: {self.id} @{self.url}"