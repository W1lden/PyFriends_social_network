import pytest
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()


@pytest.fixture
def user1(db):
    return User.objects.create_user(username="Alex", password="12345")


@pytest.fixture
def user2(db):
    return User.objects.create_user(username="Jack", password="12345")


@pytest.fixture
def admin(db):
    return User.objects.create_superuser(
        username="admin", password="12345", email="admin@gmail.com"
    )


@pytest.fixture
def authenticated_user1(client, user1):
    client.login(username="Alex", password="12345")
    return client


@pytest.fixture
def authenticated_user2(client, user2):
    client.login(username="Jack", password="12345")
    return client


@pytest.fixture
def authenticated_admin(client, admin):
    client.login(username="admin", password="12345")
    return client


@pytest.fixture
def post_user1(user1):
    return Post.objects.create(
        title='user1 wrote this title',
        text='user1 wrote this text', author=user1
    )


@pytest.fixture
def post_user2(user2):
    return Post.objects.create(
        title='user2 wrote this title',
        text='user2 wrote this text', author=user2
    )
