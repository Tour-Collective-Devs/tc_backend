from rest_framework import serializers
from api.models import Event
from .crew_member_serializer import CrewMemberSerializer
from .employer_serializer import EmployerSerializer

"""
    module: event serializer
    author: riley mathews
    purpose: to create the serializer class for the events model to expose it in the api
"""

class EventSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the event class
    """
    crew_member = CrewMemberSerializer(many=True, read_only=True)
    employer = EmployerSerializer(many=False, read_only=True)

    class Meta:
        fields = (
            'id',
            'url',
            'name',
            'employer',
            'genres',
            'role',
            'start_date',
            'end_date',
            'description',
            'total_pay',
            'show_count',
            'required_experience',
            'pay_type',
            'crew_member',
        )
        model = Event