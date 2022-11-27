from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("anounces/", include("announces.urls")),
    path("users/", include("users.urls")),
]
