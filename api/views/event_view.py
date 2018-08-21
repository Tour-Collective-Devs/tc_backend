from rest_framework import viewsets
from api.serializers import EventSerializer
from api.models import Event

""" 
    module: event view
    author: riley mathews
    purpose: to create the view for events in the api
"""

class EventView(viewsets.ModelViewSet):
    """
    class to create the event view for the api
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

