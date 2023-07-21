from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path("", views.home,name="home"),
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),
    # this allow to use all urls for auth provided by django
    # path("authentication/", include("django.contrib.auth.urls")),
    path("authentication/", include("authentication.urls")),
]
