from rest_framework import generics

from employers import models
from employers import serializers

""" 
    module: employer view
    author: riley mathews
    purpose: to generate the view for employers in api
"""

class Employer_View(generics.ListCreateAPIView):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.Employer_Serializer