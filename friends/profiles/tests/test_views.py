import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profile_view_returns_200(authenticated_client, user, user_profile):
    url = reverse("profiles:profile", kwargs={"username": user.username})
    response = authenticated_client.get(url)

    assert response.status_code == 200
    assert user.username in response.content.decode()
    assert "Test bio" in response.content.decode()


@pytest.mark.django_db
def test_profile_view_not_found(authenticated_client):
    url = reverse("profiles:profile", kwargs={"username": "nonexistentuser"})
    response = authenticated_client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_user_cannot_edit_other_profile(other_authenticated_client, user):
    url = reverse("profiles:profile_edit", kwargs={'username': user.username})
    response = other_authenticated_client.get(url)

    assert response.status_code in [302, 403]


@pytest.mark.django_db
def test_anonymous_cannot_access_profile_edit(client, user):
    url = reverse("profiles:profile_edit", kwargs={"username": user.username})
    response = client.get(url)

    assert response.status_code == 302
    assert "/login/" in response.url


@pytest.mark.django_db
def test_admin_can_view_any_profile(admin_client, user):
    url = f"/profiles/{user.username}/"
    response = admin_client.get(url)
    assert response.status_code == 200
    assert "Профиль пользователя" in response.content.decode("utf-8")
