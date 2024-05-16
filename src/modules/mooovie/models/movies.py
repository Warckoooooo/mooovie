# models.py

from django.db import models


class Movie(models.Model):
    original_title = models.CharField(max_length=255)
    english_title = models.CharField(max_length=255)
    release_date = models.DateField()
    summary = models.TextField()
    is_adult = models.BooleanField()

    # Relations
    original_language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='original_language_movies')
    languages = models.ManyToManyField('Language', related_name='movies')
    genres = models.ManyToManyField('Genre')
    production_companies = models.ManyToManyField('ProductionCompany')
    keywords = models.ManyToManyField('Keyword')

    def __str__(self):
        return self.original_title


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductionCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor} as {self.character} in {self.movie}"
