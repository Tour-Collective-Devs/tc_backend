from rest_framework import viewsets
from api.serializers import EmployerSerializer
from api.models import Employer

""" 
    module: Employer view
    author: riley mathews
    purpose: to create the view for Employers in the api
"""

class EmployerView(viewsets.ModelViewSet):
    """
    class to create the event view for the api
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

