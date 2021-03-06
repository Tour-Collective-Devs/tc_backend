from rest_framework import serializers
from api.models import CrewMemberRole

"""
    module: crew member role serializer
    author: riley mathews
    purpose: to create the serializer class for the intersection table of crew memebrs to roles
"""

class CrewMemberRoleReadSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the crew member role serializer class
    """
    class Meta:
        fields = (
            'id',
            'url',
            'years_experience',
            'role',
            'crew_member',
        )
        model = CrewMemberRole
        depth = 1