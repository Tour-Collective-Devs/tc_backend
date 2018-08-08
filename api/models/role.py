from django.db import models

""" 
    module: role model
    author: riley mathews
    purpose: to create the data model for crew roles
"""

class Role(models.Model):
    """ class to hold the data model for crew roles"""
    name = models.CharField(default="", max_length=50)
    description = models.CharField(default="", max_length=200)

    def __str__(self):
        return f'{self.name}'