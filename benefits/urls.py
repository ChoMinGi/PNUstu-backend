from django.urls import path
from . import views


urlpatterns = [
    path("", views.Benefits.as_view()),
]
