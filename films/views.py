from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Film
from .forms import FilmForm


def film_list(request):
    """Список всех фильмов с пагинацией и поиском"""
    films = Film.objects.all()
    
    # Поиск по названию фильма или описанию
    search_query = request.GET.get('search')
    if search_query:
        films = films.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(review_text__icontains=search_query)
        )
    
    # Пагинация
    paginator = Paginator(films, 10)  # 10 фильмов на страницу
    page_number = request.GET.get('page')
    films_page = paginator.get_page(page_number)
    
    context = {
        'films': films_page,
        'search_query': search_query,
    }
    
    return render(request, 'films/film_list.html', context)


def film_detail(request, pk):
    """Детальная информация о фильме"""
    film = get_object_or_404(Film, pk=pk)
    
    context = {
        'film': film,
    }
    
    return render(request, 'films/film_detail.html', context)


def film_create(request):
    """Создание нового фильма"""
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            messages.success(request, f'Фильм "{film.title}" успешно добавлен!')
            return redirect('films:film_detail', pk=film.pk)
    else:
        form = FilmForm()
    
    context = {
        'form': form,
        'title': 'Добавить фильм'
    }
    
    return render(request, 'films/film_form.html', context)


def film_edit(request, pk):
    """Редактирование фильма"""
    film = get_object_or_404(Film, pk=pk)
    
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            film = form.save()
            messages.success(request, f'Фильм "{film.title}" успешно обновлен!')
            return redirect('films:film_detail', pk=film.pk)
    else:
        form = FilmForm(instance=film)
    
    context = {
        'form': form,
        'film': film,
        'title': 'Редактировать фильм'
    }
    
    return render(request, 'films/film_form.html', context)


def film_delete(request, pk):
    """Удаление фильма"""
    film = get_object_or_404(Film, pk=pk)
    
    if request.method == 'POST':
        film_title = film.title
        film.delete()
        messages.success(request, f'Фильм "{film_title}" успешно удален!')
        return redirect('films:film_list')
    
    context = {
        'film': film,
    }
    
    return render(request, 'films/film_confirm_delete.html', context)