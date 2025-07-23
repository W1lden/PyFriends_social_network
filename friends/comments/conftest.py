import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from posts.models import Post
from comments.models import Comment

User = get_user_model()

@pytest.fixture
def user():
    return User.objects.create_user(username="user", password="123")

@pytest.fixture
def other_user():
    return User.objects.create_user(username="other", password="456")

@pytest.fixture
def admin_user():
    return User.objects.create_superuser(username="admin", password="admin123", email="admin@example.com")

@pytest.fixture
def authenticated_client(user):
    client = Client()
    client.force_login(user)
    return client

@pytest.fixture
def admin_client(admin_user):
    client = Client()
    client.force_login(admin_user)
    return client

@pytest.fixture
def post(user):
    return Post.objects.create(title="Test post", text="Sample text", author=user)

@pytest.fixture
def comment(post, user):
    return Comment.objects.create(post=post, author=user, text="Some comment")
