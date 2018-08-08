from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('role', views.Role_View, base_name='Roles')
urlpatterns = router.urls