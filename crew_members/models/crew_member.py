from django.contrib.auth.models import AbstractUser
from django.db import models
from api.models import Role

"""
    module: crew member user model
    author: jacob smith
    purpose: to create a custom model for the crew member user that uses authentication
"""

class Crew_Member(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    roles = models.ForeignKey('Role', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    location = models.CharField(blank=True, max_length=255)
    will-travel = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
