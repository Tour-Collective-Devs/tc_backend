from rest_framework import generics

from employers import models
from employers import serializers

class Employer_View(generics.ListCreateAPIView):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.Employer_Serializer