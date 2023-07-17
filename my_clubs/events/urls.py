from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="events"),
    path('<int:year>/<str:month>/', views.home,name="cal"),
    path('add_venue/', views.add_venue,name="add-venue"),
    path('venues/<venue_id>', views.venue_item,name="venue_item"),
    path('venues/', views.list_venue,name="venues_list"),
    path('search/', views.search,name="search"),
]