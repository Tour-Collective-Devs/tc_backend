from rest_framework import viewsets
from api.serializers import CrewMemberRoleSerializer, CrewMemberRoleReadSerializer
from api.models import CrewMemberRole, CrewMember
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

"""
    module: crew member role view
    author: riley mathews
    purpose: to create the view for crew member roles in the api
"""

class CrewMemberRoleView(viewsets.ModelViewSet):
    """
    class to create the crew member role view for the api
    """
    queryset = CrewMemberRole.objects.all()
    serializer_class = CrewMemberRoleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        serializer = CrewMemberRoleSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(crew_member=request.user.crew_member)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if self.request.query_params.get('crew_member'):
            crew_member = CrewMember.objects.get(id=self.request.query_params.get('crew_member', None))
            queryset = CrewMemberRole.objects.filter(crew_member=crew_member)
        else:
            queryset = CrewMemberRole.objects.all()

        return queryset

    def get_serializer_class(self):

        if self.request.method in ['GET']:

            return CrewMemberRoleReadSerializer

        return CrewMemberRoleSerializer
