from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.http import JsonResponse
from django.db.utils import IntegrityError
from .forms import searchForm, addForm, searchWatchlistForm, isWatchedForm
import json
from .models import watchedlist, Movie
import omdb
from pprint import pprint



def search(request):
    context = {
        "search_results": {},
    }

    if request.method == "POST":
        form = searchForm(request.POST)
        if form.is_valid():
            title = form.data['title']
        search_results = omdb.search(title)
        context["search_results"] = search_results

    return render(request, "index.html", context)


def add(request):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            titles = form.data.lists()[1][1]
            for title in titles:
                movie = omdb.title(title)
                try:
                    Movie.objects.create(
                        title=movie.title,
                        genre=movie.genre,
                        actors=movie.actors,
                        imdb_id=movie.imdb_id)
                except IntegrityError:
                    pass
    return redirect('search')


def watchlist(request):
    if request.method == "POST":
        form = isWatchedForm()
        if form.is_valid():
            movie = Movie.objects.get(form.data['imdb_id'])
    else:
        movies = Movie.objects.all()

    return render(request, "watchlist.html", {'movies': movies})


def search_watchlist(request):
    if request.method == "POST":
        form = searchWatchlistForm()
        if form.is_valid():
            movies = Movie.objects.filter(**form.data)
        else:
            movies = {}
    else:
        movies = {}

    return render(request, "search_watchlist.html", {'movies': movies})

"""def deleteMovie(request):
    if request.method == "POST":
        form = isWatchedForm()
        if form.is_valid():
            movie = Movie.objects.deleteMovie()

    return redirect('watchlist')"""