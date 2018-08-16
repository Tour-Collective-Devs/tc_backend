from rest_framework import serializers
from crew_members import models

"""
    module: crew member serializer
    author: jacob smith
    purpose: to create the serializer for the crew member model
"""

class Crew_Member_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Crew_Member
        fields = ('email', 'username', 'id', 'url', 'name' )