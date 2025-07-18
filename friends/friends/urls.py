from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from posts import urls as posts_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(posts_urls)),
    path("users/", include("users.urls")),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
