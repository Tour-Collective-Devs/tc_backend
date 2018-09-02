from rest_framework import viewsets
from api.serializers import RoleSerializer
from api.models import Role

"""
    module: role view
    author: riley mathews
    purpose: to create a view and endpoint for the crew member roles resource
"""

class RoleView(viewsets.ModelViewSet):
    """
    API endpoint that allows role to be viewed or edited.
    Author: riley mathews
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


