import random

import requests
from django.conf import settings
from django.shortcuts import render


def get_movie_by_id(api_key, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_random_movies(api_key, count):
    movies = []
    for _ in range(count):
        movie_id = random.randint(1, 128188)  # Générer un ID aléatoire dans la plage
        movie = get_movie_by_id(api_key, movie_id)
        if movie:
            movies.append(movie)
    return movies


def index(request):
    api_key = settings.TMDB_API_KEY
    movies = get_random_movies(api_key, 20)
    return render(request, 'index.html', {'movies': movies})
