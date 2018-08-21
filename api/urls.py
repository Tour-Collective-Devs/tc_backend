from api import views
from employers.views import EmployerView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()

urlpatterns = [
    path('employer-auth/', include('rest_auth.urls')),
    path('employer/registration/', include('rest_auth.registration.urls')),
]

router.register('employer', EmployerView, base_name='employer')
router.register('genre', views.GenreView, base_name='genre')
router.register('role', views.RoleView, base_name='role')
router.register('event', views.EventView, base_name='event')

urlpatterns += router.urls
