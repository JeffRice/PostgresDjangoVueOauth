from rest_framework import serializers
from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    oauthcredentials = models.CharField(max_length=1000)

    def __str__(self):
        return self.email

