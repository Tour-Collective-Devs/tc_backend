from rest_framework import viewsets
from api.serializers import CrewMemberRoleSerializer
from api.models import CrewMemberRole
from rest_framework.permissions import IsAuthenticatedOrReadOnly

"""
    module: crew member role view
    author: riley mathews
    purpose: to create the view for crew member roles in the api
"""

class CrewMemberRoleView(viewsets.ModelViewSet):
    """
    class to create the crew member role view for the api
    """
    queryset = CrewMemberRole.objects.all()
    serializer_class = CrewMemberRoleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)