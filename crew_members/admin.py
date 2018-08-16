from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import Crew_Member_Creation_Form, Crew_Member_Change_Form
from .models import Crew_Member

class Crew_Member_User_Admin(UserAdmin):
    add_form = Crew_Member_Creation_Form
    form = Crew_Member_Change_Form
    model = Crew_Member
    list_display = ['email', 'username', 'name']

admin.site.register(Crew_Member, Crew_Member_User_Admin)