from .views import Genre_View
from api import views
from employers.views import Employer_View
from crew_members.views import Crew_Member_View
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()

urlpatterns = [
    path('employer-auth/', include('rest_auth.urls')),
    path('employer/registration/', include('rest_auth.registration.urls')),
]

router.register('employer', Employer_View, base_name='employer')
router.register('crew', Crew_Member_View, base_name='crew')
router.register('genre', Genre_View, base_name='genre')
router.register('role', views.Role_View, base_name='role')
router.register('event', views.Event_View, base_name='event')

urlpatterns += router.urls
