from rest_framework import viewsets
from api.serializers import EventSerializer, EventReadSerializer
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

    def get_queryset(self):
        if self.request.query_params.get('employer', False) and self.request.user.is_employer:
            queryset = Event.objects.filter(employer=self.request.user.employer)
        else:
            queryset = Event.objects.all()

        return queryset

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            
            return EventReadSerializer
            
        return EventSerializer