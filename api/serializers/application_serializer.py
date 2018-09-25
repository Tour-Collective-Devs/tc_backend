from rest_framework import serializers
from api.models import Application

"""
    module: application serializer
    author: jacob smith
    purpose: to create the serializer class for the applications model to expose it in the api
"""

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the employer class
    """
    class Meta:
        fields = (
            'id',
            'url',
            'accepted',
            'crew_member',
            'event'
        )
        model = Application