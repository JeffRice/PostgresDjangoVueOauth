from django.db import models

# Create your models here.
class Note(models.Model):
    token = models.TextField()
    user = models.TextField()