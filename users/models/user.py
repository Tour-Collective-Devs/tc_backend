# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

""" 
    module: employer user model
    author: riley mathews
    purpose: to create a custom model for the employer user that uses authentication
"""

class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
