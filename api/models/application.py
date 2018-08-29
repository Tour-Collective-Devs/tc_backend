from django.db import models
from . import CrewMember
from . import Event


class Application(models.Model):
    """
    Joining table using CrewMember and Event for crew member applications
    Author: Jacob Smith

    """
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.event.name}'



