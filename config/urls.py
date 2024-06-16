from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("noti/", include("noti.urls")),
    path("admin/", admin.site.urls),
]
