from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "test_anonymous_page/",
        views.test_anonymous_page,
        name="test_anonymous_page"
    ),
]
