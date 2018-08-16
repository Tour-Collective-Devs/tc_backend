from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()

from . import views

router.register('', views.Employer_View)

urlpatterns = router.urls