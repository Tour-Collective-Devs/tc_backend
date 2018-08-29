from rest_framework import serializers
from api.models import Employer
from users.serializers import UserSerializer

"""  
    module: event serializer
    author: riley mathews
    purpose: to create the serializer class for the employers model to expose it in the api
"""

class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the employer class
    """

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        fields = (
            'id',
            'url',
            'organization_name',
            'user',
        )
        model = Employer

