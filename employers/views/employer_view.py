from rest_framework import generics

from . import models
from . import serializers

class Employer_View(generics.ListCreateAPIView):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.Employer_Serializer