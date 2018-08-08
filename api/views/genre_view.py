from rest_framework import viewsets
from api.serializers import Genre_Serializer
from api.models import Genre

class Genre_View(viewsets.ModelViewSet):
    """
    API endpoint that allows Genre to be viewed or edited.
    Author: Jacob Smith
    """
    queryset = Genre.objects.all()
    serializer_class = Genre_Serializer

