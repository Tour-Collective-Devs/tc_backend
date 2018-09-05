from django.db import models
from .crew_member import CrewMember
from .role import Role

"""  
    module crew member role
    author riley mathews
    purpose to create intersection table for crew member to roles
"""

class CrewMemberRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    years_experience = models.IntegerField(blank=True, null=True)