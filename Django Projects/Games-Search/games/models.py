from django.db import models


class Games(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    editors_choice = models.CharField(max_length=20)

# Create your models here.
