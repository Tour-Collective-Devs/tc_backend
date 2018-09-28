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

    """
    author: jacob smith
    purpose: Determine the current user by their token, and return their data
    """
    def get_queryset(self):

        crew_id = self.request.query_params.get("id", None)

        if crew_id:
            queryset = CrewMember.objects.filter(pk=crew_id)
        else:
            queryset = CrewMember.objects.filter(id=self.request.user.crew_member.id)
        return queryset


