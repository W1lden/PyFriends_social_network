from comments import urls as comments_urls
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from posts import urls as posts_urls
from profiles import urls as profiles_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(posts_urls)),
    path("", include(comments_urls)),
    path("users/", include("users.urls")),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profiles/", include(profiles_urls)),
]
