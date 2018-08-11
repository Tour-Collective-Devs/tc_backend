from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from employers.models import Employer

class Employer_Creation_Form(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Employer
        fields = ('username', 'email')

class Employer_Change_Form(UserChangeForm):

    class Meta:
        model = Employer
        fields = UserChangeForm.Meta.fields