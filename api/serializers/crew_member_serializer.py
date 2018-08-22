from rest_framework import serializers
from api.models import CrewMember

class CrewMemberSerializer(serializers.HyperlinkedModelSerializer):
    """
    CrewMember serializer that takes the CrewMember model and serializes to be JSON formatted and readable.
    Author: Jacob Smith
    """
    class Meta:
        fields = (
            'id',
            'roles',
            'user',
            'verified',
            'city',
            'state',
            'will_travel'
        )
        model = CrewMember