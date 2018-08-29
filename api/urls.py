from api import views
from users.views import UserView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()

urlpatterns = [
    path('user-auth/', include('rest_auth.urls')),
    path('user/registration/', include('rest_auth.registration.urls')),
]

router.register('user', UserView, base_name='user')
router.register('genre', views.GenreView, base_name='genre')
router.register('role', views.RoleView, base_name='role')
router.register('event', views.EventView, base_name='event')
router.register('crew_member', views.CrewMemberView, base_name='crewmember')
router.register('crew_member_role', views.CrewMemberRoleView, base_name='crewmemberrole')
router.register('employer', views.EmployerView, base_name='employer')
router.register('application', views.ApplicationView, base_name='application')

urlpatterns += router.urls
