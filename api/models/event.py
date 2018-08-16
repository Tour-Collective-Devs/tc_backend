from django.db import models
from employers.models import Employer
from api.models import Genre
from api.models import Role

"""  
    module: event model
    author: riley mathews
    purpose: to create the data model for events
"""

class Event(models.Model):
    """ 
        Class for creating the event data model. 
    """
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    name = models.CharField(default="", max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)
    total_pay = models.IntegerField()
    show_count = models.IntegerField()
    required_experience = models.CharField(max_length=500)
    pay_types = (
        ("day", "Dailey"),
        ("upfront", "Up Front")
    )
    pay_type = models.CharField(max_length=20, choices=pay_types)

    def __str__(self):
        """str method for genre class
        
        Returns:
            str -- name of event
        """
        return f'{self.name}'