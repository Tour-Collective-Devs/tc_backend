from .views import Genre_View
from .views import Employer_View
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('genre', Genre_View, base_name='genre')
router.register('employer', Employer_View, base_name='employer')

urlpatterns = router.urls
