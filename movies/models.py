from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class Movie(models.Model):
    title = models.CharField(max_length=256)
    year = models.CharField(max_length=256)
    runtime = models.CharField(max_length=256)
    rated = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    actors = models.CharField(max_length=256)
    plot = models.TextField(max_length=256)
    language = models.CharField(max_length=256)
    awards = models.CharField(max_length=256)
    poster = models.CharField(max_length=256)
    rotten_tomato = models.CharField(max_length=256)
    imdb = models.CharField(max_length=256)
    metacritic = models.CharField(max_length=256)

    likes = models.IntegerField(default=0)
    vetos = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies_seen = models.ManyToManyField(Movie)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
