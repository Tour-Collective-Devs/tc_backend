from rest_framework import serializers
from . import models

class Employer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = ('email', 'username', )