from django.urls import path
from .views import profile_view, edit_profile

app_name = "profiles"

urlpatterns = [
    path("edit/", edit_profile, name="edit_profile"),
    path("<str:username>/", profile_view, name="profile"),
]
