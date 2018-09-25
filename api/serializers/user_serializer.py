from rest_framework import serializers
from api.models import User

"""
    module: employer serializer
    author: riley mathews
    purpose: to create the serializer for the employer model
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'id', 'url', 'first_name', 'last_name', 'is_crew_member', 'is_employer')