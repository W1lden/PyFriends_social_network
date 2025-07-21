from django.urls import path

from .views import edit_profile, profile_view

app_name = "profiles"

urlpatterns = [
    path("edit/", edit_profile, name="edit_profile"),
    path("<str:username>/", profile_view, name="profile"),

]
