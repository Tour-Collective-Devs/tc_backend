from rest_framework import viewsets
from api.models import Role
from api.serializers import Role_Serializer

"""  
    module: role view
    author: riley mathews
    purpose: to create the view for crew member roles
"""

class Role_View(viewsets.ModelViewSet):
    """creates the view for crew member roles"""
    queryset = Role.objects.all()
    serializer_class = Role_Serializer