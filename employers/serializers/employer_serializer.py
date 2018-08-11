from rest_framework import serializers
from employers import models

class Employer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = ('email', 'username', )