from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class Employer_Creation_Form(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class Employer_Change_Form(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields