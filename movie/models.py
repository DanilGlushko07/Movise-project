from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    genre = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    time = models.IntegerField()
    grade = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Director)
