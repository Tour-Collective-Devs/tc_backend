from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_employer = serializers.BooleanField()
    is_crew_member = serializers.BooleanField()

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'is_employer': self.validated_data.get('is_employer', ''),
            'is_crew_member': self.validated_data.get('is_crew_member', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        # add custom fields
        user.is_crew_member = self.cleaned_data.get('is_crew_member')
        user.is_employer = self.cleaned_data.get('is_employer')

        user.save()

        return user