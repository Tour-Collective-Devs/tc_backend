from rest_framework import serializers
from api.models import Genre

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Genre serializer that takes the Genre model and serializes to be JSON formatted and readable.
    """
    class Meta:
        fields = (
            'id',
            'url',
            'name',
        )
        model = Genre