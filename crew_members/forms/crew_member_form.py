from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crew_members.models import Crew_Member

"""
    moduel: crew member forms
    author: jacob smith
    purpose: generates forms for crew member edit and creation
"""

class Crew_Member_Creation_Form(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Crew_Member
        fields = ('username', 'email')

class Crew_Member_Change_Form(UserChangeForm):

    class Meta:
        model = Crew_Member
        fields = UserChangeForm.Meta.fields