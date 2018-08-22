from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User

"""
    moduel: User forms
    author: riley mathews
    purpose: generates forms for User edit and creation
"""

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields