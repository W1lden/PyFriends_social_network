from comments import urls as comments_urls
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from posts import urls as posts_urls
from profiles import urls as profiles_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include(("posts.urls", "posts"), namespace="posts")),
    path("comments/", include(("comments.urls", "comments"), namespace="comments")),
    path("users/", include("users.urls")),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profiles/", include(profiles_urls)),
]
