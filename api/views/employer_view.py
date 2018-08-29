from rest_framework import viewsets
from api.serializers import EmployerSerializer
from api.models import Employer
from rest_framework import status
from rest_framework.response import Response

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

    def create(self, request):
        serializer = EmployerSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

