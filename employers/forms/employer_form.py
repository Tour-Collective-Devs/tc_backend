from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from employers.models import Employer

""" 
    moduel: employer forms
    author: riley mathews
    purpose: generates forms for employer edit and creation
"""

class Employer_Creation_Form(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Employer
        fields = ('username', 'email')

class Employer_Change_Form(UserChangeForm):

    class Meta:
        model = Employer
        fields = UserChangeForm.Meta.fields