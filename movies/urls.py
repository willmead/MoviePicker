from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('leaderboard', views.TopMoviesView.as_view(), name='top_movies')
]
