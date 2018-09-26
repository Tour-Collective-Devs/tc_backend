from django.contrib import admin
from api import models
# Register your models here.


admin.site.register(models.Application)
admin.site.register(models.CrewMember)
admin.site.register(models.CrewMemberRole)
admin.site.register(models.Employer)
admin.site.register(models.Event)
admin.site.register(models.Genre)
admin.site.register(models.User)