from django.db import models
from users.models import User

"""
    module: employer model
    author: riley mathews
    purpose: to hold the data model for employer profile
"""

class Employer(models.Model):
    """ model to hold employer profile information """
    organization_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.organization_name}'
