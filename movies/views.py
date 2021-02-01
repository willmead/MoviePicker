from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Movie
from . import imdb_scaper

import random

class TopMoviesView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'movies/top_movies.html'
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        movies = [movie for movie in Movie.objects.all() if movie.likes > 0]
        movies.sort(key=lambda x: x.likes, reverse=True)

        context.update({'movies': movies})
        return context


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'movies/index.html'
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # THIS IS ONLY FOR INITIALLY SCRAPING MOVIE DATA
        # AND IT HAS BEEN KEPT IN CASE OF EMERGENCY, DO NOT UNCOMMENT!

        # ids = imdb_scaper.get_ids()
        # for id in ids:
        #     movie_data = imdb_scaper.get_movie_data_from_id(id)
        #     movie = Movie(**movie_data)
        #     movie.save()

        random_movie = random.choice(Movie.objects.all())

        context.update({'movie': random_movie})
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        user = request.user
        movie = Movie.objects.get(pk=data["movie"])

        if "like" in data:
            print(f"Add a like to {movie}")
            user.profile.movies_seen.add(movie)
            movie.likes += 1
            movie.save()
        elif "veto" in data:
            print(f"Add a veto to {movie}")
            user.profile.movies_seen.add(movie)
            movie.vetos += 1
            movie.save()

        return self.get(self, request, *args, **kwargs)
