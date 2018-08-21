from rest_framework import viewsets

from employers import models
from employers import serializers

""" 
    module: employer view
    author: riley mathews
    purpose: to generate the view for employers in api
"""

class EmployerView(viewsets.ModelViewSet):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.EmployerSerializer