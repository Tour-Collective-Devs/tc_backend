from rest_framework import viewsets
from api.serializers import EventSerializer
from api.models import Event
from rest_framework import status
from rest_framework.response import Response

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

    def create(self, request):
        serializer = EventSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(employer=request.user.employer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)