from rest_framework import serializers
from api.models import Employer

class Employer_Serializer(serializers.HyperlinkedModelSerializer):
    """
    Employer serializer that takes the Employer model and serializes to be JSON formatted and readable.
    """
    class Meta:
        fields = (
            'id',
            'url',
            'name',
            'email',
            'password'
        )
        model = Employer