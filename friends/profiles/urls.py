from django.urls import path

from .views import profile_edit, profile_view

app_name = "profiles"

urlpatterns = [
    path("edit/", profile_edit, name="profile_edit"),
    path("<str:username>/", profile_view, name="profile"),
]
