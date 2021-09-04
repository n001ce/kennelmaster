from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='animals_index'),
    path('employees/', views.employees_index, name='employees_index'),
    path('animals/<int:animal_id>/', views.animals_detail, name='animals_detail'),
    path('employees/<int:employee_id>/', views.employees_detail, name='employees_detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('employees/create/', views.EmployeeCreate.as_view(), name='employees_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employees_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
    path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employees_delete'),
    path('animals/<int:animal_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('animals/<int:animal_id>/add_owner', views.add_owner, name='add_owner'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/' ,views.TaskDetail.as_view(), name='tasks_detail'),
    path('tasks/', views.TaskList.as_view(), name='tasks_index'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('employees/<int:employee_id>/assoc_task/<int:task_id>/', views.assoc_task, name='assoc_task'),
]

