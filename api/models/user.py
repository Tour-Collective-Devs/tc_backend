# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

"""
    module: user model
    author: riley mathews
    purpose: to create a custom model for the employer and crew member user that uses authentication
"""

class User(AbstractUser):
    is_employer = models.BooleanField(blank=True, default=0)
    is_crew_member = models.BooleanField(blank=True, default=0)

    def __str__(self):
        return self.email
