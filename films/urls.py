from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    # Основные страницы фильмов
    path('', views.film_list, name='film_list'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
    
    # CRUD операции
    path('add/', views.film_create, name='film_create'),
    path('edit/<int:pk>/', views.film_edit, name='film_edit'),
    path('delete/<int:pk>/', views.film_delete, name='film_delete'),
]
