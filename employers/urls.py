from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Employer_View.as_view()),
]