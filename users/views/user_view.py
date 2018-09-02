from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from users import models
from users import serializers

"""
    module: employer view
    author: riley mathews
    purpose: to generate the view for employers in api
"""

class UserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):

        queryset = models.User.objects.filter(id=self.request.user.id)
        print(self.request.user)
        return queryset