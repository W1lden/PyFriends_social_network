from django.urls import path
from posts.views import home_page

app_name = "posts"

urlpatterns = [
    path("", home_page, name="home"),
]
