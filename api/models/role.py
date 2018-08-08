from django.db import models

""" 
    modue: role model
    author: riley mathews
    purpose: create the data model for a crew member role
"""

class Role(models.Model):
    """this class contains the data model for crew member roles"""
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=300, default="")