from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import Employer_Creation_Form, Employer_Change_Form
from .models import Employer

class Employer_User_Admin(UserAdmin):
    add_form = Employer_Creation_Form
    form = Employer_Change_Form
    model = Employer
    list_display = ['email', 'username', 'name']

admin.site.register(Employer, Employer_User_Admin)