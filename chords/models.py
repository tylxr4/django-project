from django.db import models

# Create your models here.
class Chord(models.Model):
    name = models.CharField(max_length=100)
    key = models.TextField()
    tabs = models.CharField(max_length=400)
    difficulty = models.TextField()
