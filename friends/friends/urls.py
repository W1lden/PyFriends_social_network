from django.contrib import admin
from django.urls import include, path
from posts import urls as posts_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(posts_urls)),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]
