import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


def test_anonymous_cannot_see_secured_page(client):
    """Тест: аноним не видит защищённую страницу"""
    url = reverse("test_anonymous_page")
    response = client.get(url)

    assert response.status_code == 302
    assert "/login/" in response.headers["Location"]


@pytest.mark.django_db
def test_register_view(client):
    """Тест: пользователь регистрируется и видит нужную страницу"""
    response = client.post(
        reverse("register"),
        {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
        },
    )

    assert response.status_code == 302
    assert User.objects.filter(username="testuser").exists()

    client.login(username="testuser", password="strongpassword123")

    url = reverse("test_anonymous_page")
    response = client.get(url)

    assert response.status_code == 200
    assert response.request["PATH_INFO"] == reverse("test_anonymous_page")


@pytest.mark.django_db
def test_login_view(client, django_user_model):
    """Тест: логин/логаут работают"""
    django_user_model.objects.create_user(username="tester", password="pass12345")

    response = client.post(
        reverse("login"), {"username": "tester", "password": "pass12345"}
    )

    assert response.status_code == 302
    assert "_auth_user_id" in client.session

    response = client.post(reverse("logout"))

    assert response.status_code == 302
    assert "_auth_user_id" not in client.session


@pytest.mark.django_db
def test_invalid_password(client, django_user_model):
    """Тест: неправильный пароль не даёт входа"""
    django_user_model.objects.create_user(username="tester", password="pass12345")

    response = client.post(
        reverse("login"), {"username": "tester", "password": "invalid_pass"}
    )

    assert response.status_code == 200
    assert "_auth_user_id" not in client.session


@pytest.mark.django_db
def test_session_save_after_login(client, django_user_model):
    """Тест: сессия сохраняется после входа"""
    django_user_model.objects.create_user(username="tester", password="pass12345")

    response = client.post(
        reverse("login"), {"username": "tester", "password": "pass12345"}
    )

    assert response.status_code == 302
    assert "_auth_user_id" in client.session
