from __future__ import unicode_literals

from django.db import models


class watchedlist(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    watched_date = models.DateTimeField('Watched date')

    def __str__(self):
        return str.title


class Movie(models.Model):
    verbose_name = "Movie"
    verbose_name_plural = "Movies"
    imdb_id = models.CharField(max_length=10, unique=True, default='')
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    actors = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
