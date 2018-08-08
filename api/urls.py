from .views import Genre_View
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('genre', Genre_View, base_name='genre')

urlpatterns = router.urls
