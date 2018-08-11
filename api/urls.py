from .views import Genre_View
# from .views import Employer_View
from api import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()

urlpatterns = [
    path('employer', include('employers.urls')),
    path('employer/auth', include('rest_auth.urls')),
    path('employer/registration/', include('rest_auth.registration.urls')),
]



router.register('genre', Genre_View, base_name='genre')
# router.register('employer', Employer_View, base_name='employer')
router.register('role', views.Role_View, base_name='role')

urlpatterns += router.urls
