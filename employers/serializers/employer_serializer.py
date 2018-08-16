from rest_framework import serializers
from employers import models

""" 
    module: employer serializer
    author: riley mathews
    purpose: to create the serializer for the employer model
"""

class Employer_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employer
        fields = ('email', 'username', 'id', 'url', 'name')