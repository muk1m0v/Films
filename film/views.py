from django.shortcuts import render, redirect
from . import models

def home(request):
    films = models.Films.objects.all()
    return render(request, 'index.html',context={'films':films})

def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')
        poster = request.FILES.get('poster')
        caption = request.POST.get('caption')
        genre_id = request.POST.get('genre')
        genre = models.Genre.objects.filter(id=genre_id).first()
        film = models.Films.objects.create(
            title=title, caption=caption, release_year=release_year, rating=rating, poster=poster, genre=genre
        )
        return redirect('detail_film', pk=film.id)
    genreis = models.Genre.objects.all()
    return render(request, 'create_film.html', {'genreis': genreis})

def detail_film(request, pk):
    films = models.Films.objects.get(id=pk)
    return render(request, 'film-detail.html', context={'film':films})

def update_film(request, pk):
    film = models.Films.objects.get(id=pk)
    if request.method == 'POST':
        film.title = request.POST.get('title')
        film.caption = request.POST.get('caption')
        film.release_year = request.POST.get('release_year')
        film.rating = request.POST.get('rating')
        film.poster = request.FILES.get('poster')
        genre_id = request.POST.get('genre')
        film.genre = models.Genre.objects.filter(id=genre_id).first()
        film.save()
        return redirect('detail_film', pk=film.id)
    genreis = models.Genre.objects.all()
    return render(request, 'update_film.html', context={'film': film, 'genreis': genreis})

def delete_film(request, pk):
    film = models.Films.objects.get(id=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('home')
    return render(request, 'delete_film.html', context={'film': film})

def create_genre(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        models.Genre.objects.create(name=name)
        return redirect('home')
    return render(request, 'create_genre.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        models.FeedBack.objects.create(name=name, message=message)
        return redirect('contacts')
    return render(request, 'contacts.html')

def feedbacks(request):
    feedbacks = models.FeedBack.objects.all()
    return render(request, 'feedbacks.html', context={'feedbacks': feedbacks})

def genres(request):
    genres = models.Genre.objects.all()
    return render(request, 'genre.html', context={'genres': genres})