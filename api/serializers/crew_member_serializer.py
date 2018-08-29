from rest_framework import serializers
from api.models import CrewMember
from users.serializers import UserSerializer

class CrewMemberSerializer(serializers.HyperlinkedModelSerializer):
    """
    CrewMember serializer that takes the CrewMember model and serializes to be JSON formatted and readable.
    Author: Jacob Smith
    """

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = CrewMember
        depth = 1