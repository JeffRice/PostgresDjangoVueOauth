from django.db import models

# Create your models here.
class Note(models.Model):
    selectedRepo = models.TextField()
    token = models.TextField()
    user = models.TextField()