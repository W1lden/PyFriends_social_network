import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser", password="testpass123"
    )


@pytest.fixture
def user_profile(user):
    profile = user.userprofile
    profile.bio = "Test bio"
    profile.birth_date = "2000-01-01"
    profile.save()
    return profile


@pytest.fixture
def authenticated_client(client, user):
    client.login(username="testuser", password="testpass123")
    return client


@pytest.fixture
def other_user(db):
    return User.objects.create_user(username="other", password="otherpass")


@pytest.fixture
def other_authenticated_client(client, other_user):
    client.login(username="other", password="otherpass")
    return client


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        username="admin",
        password="adminpass"
    )


@pytest.fixture
def admin_client(client, admin_user):
    client.login(username="admin", password="adminpass")
    return client
