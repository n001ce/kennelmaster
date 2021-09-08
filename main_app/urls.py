from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),    
    path('about/', views.about, name='about'),
    path('profiles/<int:user_id>/', views.profiles_detail, name='profiles_detail'),
    path('animals/', views.animals_index, name='animals_index'),
    path('animals/<int:animal_id>/', views.animals_detail, name='animals_detail'),
    path('animals/<int:user_id>/', views.animals_detail, name='user_animal'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
    path('animals/<int:animal_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/' ,views.TaskDetail.as_view(), name='tasks_detail'),
    path('tasks/', views.TaskList.as_view(), name='tasks_index'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

