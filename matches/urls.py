from django.urls import path
from . import views

urlpatterns = [
    path("", views.match_list, name="match_list"),
    path("match/<int:match_id>/", views.match_detail, name="match_detail"),
    path("scrape/", views.scrape_and_update, name="scrape_and_update"),
]
