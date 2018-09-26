from api import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()

urlpatterns = [
    path('auth/register/', views.register_user),
    path('auth/login/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router.register('user', views.UserView, base_name='user')
router.register('genre', views.GenreView, base_name='genre')
router.register('role', views.RoleView, base_name='role')
router.register('event', views.EventView, base_name='event')
router.register('crew_member', views.CrewMemberView, base_name='crewmember')
router.register('crew_member_role', views.CrewMemberRoleView, base_name='crewmemberrole')
router.register('employer', views.EmployerView, base_name='employer')
router.register('application', views.ApplicationView, base_name='application')

urlpatterns += router.urls
