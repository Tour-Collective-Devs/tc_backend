from django.db import models
from api.models import Role
from .user import User

"""
    module: crew_member model
    author: jacob smith
    purpose: to create a custom model for the crew member that uses authentication via a one to one field with User
"""
class CrewMember(models.Model):
    roles = models.ManyToManyField(Role, through='CrewMemberRole', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='crew_member')
    verified = models.BooleanField(default=False, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    will_travel = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

