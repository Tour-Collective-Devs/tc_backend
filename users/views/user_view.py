from rest_framework import viewsets

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