from rest_framework import viewsets

from crew_members import models
from crew_members import serializers

"""
    module: crew_member view
    author: jacob smith
    purpose: to generate the view for crew members in the api
"""

class Employer_View(viewsets.ModelViewSet):
    queryset = models.Crew_Member.objects.all()
    serializer_class = serializers.Crew_Member_Serializer

