from rest_framework import viewsets
from api.serializers import ApplicationSerializer
from api.models import Application

"""
    module: Application view
    author: jacob smith
    purpose: to create the view for Employers in the api
"""

class ApplicationView(viewsets.ModelViewSet):
    """
    class to create the event view for the api
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer