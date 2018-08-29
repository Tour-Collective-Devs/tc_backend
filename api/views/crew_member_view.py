from rest_framework import viewsets
from api.serializers import CrewMemberSerializer
from api.models import CrewMember
from rest_framework import status
from rest_framework.response import Response

"""
    module: crew member view
    author: jacob smith
    purpose: to create the view for crew members in the api
"""

class CrewMemberView(viewsets.ModelViewSet):
    """
    class to create the crew member view for the api
    """
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

    def create(self, request):
        serializer = CrewMemberSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
