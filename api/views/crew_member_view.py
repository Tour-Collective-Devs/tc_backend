from rest_framework import viewsets
from api.serializers import CrewMemberSerializer
from api.models import CrewMember

"""
    module: crew member view
    author: jacob smith
    purpose: to create the view for crew members in the api
"""

class CrewMemberView(viewsets.ModelViewSet):
    """
    class to create the crew member view for the api
    """
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

