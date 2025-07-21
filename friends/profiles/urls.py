from django.urls import path
from .views import profile_view, profile_edit


app_name = "profiles"

urlpatterns = [
    path("edit/", profile_edit, name="profile_edit"),
    path("<str:username>/", profile_view, name="profile"),
]
