from rest_framework import serializers
from api.models import Event

"""  
    module: event serializer
    author: riley mathews
    purpose: to create the serializer class for the events model to expose it in the api
"""

class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the event class
    """
    class Meta:
        fields = (
            'id',
            'url',
            'user',
            'genres',
            'role',
            'start_date',
            'end_date',
            'description',
            'total_pay',
            'show_count',
            'required_experience',
            'pay_type',
        )
        model = Event