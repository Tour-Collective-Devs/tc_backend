from rest_framework import viewsets
from api.serializers import Event_Serializer
from api.models import Event

""" 
    module: event view
    author: riley mathews
    purpose: to create the view for events in the api
"""

class Event_View(viewsets.ModelViewSet):
    """
    class to create the event view for the api
    """
    queryset = Event.objects.all()
    serializer_class = Event_Serializer

