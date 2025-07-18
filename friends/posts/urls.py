from django.urls import path
from posts.views import (all_posts, home_page, post_create, post_delete,
                         post_detail, post_edit)

app_name = "posts"

urlpatterns = [
    path("", home_page, name="home"),
    path("posts/", all_posts, name="all_posts"),
    path("posts/<int:post_id>", post_detail, name="post_detail"),
    path("posts/<int:post_id>/delete", post_delete, name="post_delete"),
    path("posts/<int:post_id>/edit", post_edit, name="post_edit"),
    path("posts/create", post_create, name="post_create")
]
