from django.urls import path
from . import views


urlpatterns = [
    path("", views.Announces.as_view()),
]
