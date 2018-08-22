from django.db import models

"""
    module: crew_member model
    author: jacob smith
    purpose: to create a custom model for the crew member that uses authentication via a one to one field with User
"""
class CrewMember(models.Model):
    