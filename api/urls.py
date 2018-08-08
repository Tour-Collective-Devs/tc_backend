from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('genre', views.Genre_View, base_name='genre')
router.register('role', views.Role_View, base_name='role')

urlpatterns = router.urls
