from rest_framework import serializers
from api.models import Employer

"""  
    module: event serializer
    author: riley mathews
    purpose: to create the serializer class for the employers model to expose it in the api
"""

class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the employer class
    """
    class Meta:
        fields = (
            __all__
        )
        model = Employer