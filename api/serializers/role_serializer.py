from rest_framework import serializers
from api.models import Role

"""  
    module: role serializer
    author: riley mathews
    purpose: to create the serializer for the crew member role model
"""

class Role_Serializer(serializers.ModelSerializer):
    """serializer for crew member roles"""
    class Meta:
        fields = (
            'name',
            'description'
        )
        model = Role