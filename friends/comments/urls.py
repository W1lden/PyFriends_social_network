from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("comments/delete/<int:pk>/", views.delete_comment, name="comment_delete"),
]
