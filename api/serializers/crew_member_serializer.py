from rest_framework import serializers
from api.models import CrewMember
from .user_serializer import UserSerializer

class CrewMemberSerializer(serializers.HyperlinkedModelSerializer):
    """
    CrewMember serializer that takes the CrewMember model and serializes to be JSON formatted and readable.
    Author: Jacob Smith
    """

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        fields = (
            'id',
            'url',
            'user',
            'verified',
            'city',
            'state',
            'will_travel',
        )
        model = CrewMember
        depth = 1