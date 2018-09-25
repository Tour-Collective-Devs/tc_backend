from rest_framework import serializers
from api.models import CrewMemberRole
from .crew_member_role_read_serializer import CrewMemberRoleReadSerializer

"""
    module: crew member role serializer
    author: riley mathews
    purpose: to create the serializer class for the intersection table of crew memebrs to roles
"""

class CrewMemberRoleSerializer(serializers.HyperlinkedModelSerializer):
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
        # depth = 1

    def to_representation(self, instance):
        serializer = CrewMemberRoleReadSerializer(instance, context=self.context)
        return serializer.data