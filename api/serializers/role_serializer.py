from rest_framework import serializers
from api.models import Role

""" 
    module: role serializer
    author: riley mathews
    purpose: to hold the serializer for the crew member roles
"""

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Role Serializer that will take the role and format it into python data
    """
    class Meta:
        fields = (
            'id',
            'url',
            'name',
            'description',
        )
        model = Role