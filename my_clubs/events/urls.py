from django.contrib import admin
from django.urls import path
from . import views

# learn about path converters

urlpatterns = [
    path('<int:year>/<str:month>/', views.home),
]
