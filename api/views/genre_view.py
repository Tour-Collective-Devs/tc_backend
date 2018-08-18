from rest_framework import viewsets
from api.serializers import GenreSerializer
from api.models import Genre

class GenreView(viewsets.ModelViewSet):
    """
    API endpoint that allows Genre to be viewed or edited.
    Author: Jacob Smith
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

