from http import HTTPStatus

import pytest
from django.urls import reverse
from posts.models import Post


# Тест 1: главная открывается у всех
@pytest.mark.django_db
def test_home_page_accessible(client):
    url = reverse("posts:home")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert "Добро пожаловать" in response.content.decode()


# Тест 2: Аноним видит Вход/Регистрация
@pytest.mark.django_db
def test_anonymous_user_sees_login_links(client):
    url = reverse("posts:home")
    response = client.get(url)
    content = response.content.decode()
    assert "Вход" in content
    assert "Регистрация" in content
    assert "Профиль" not in content


# Тест 3: Авторизованный видит Профиль/Выход
@pytest.mark.django_db
def test_authenticated_user_sees_profile(authenticated_user1):
    url = reverse("posts:home")
    response = authenticated_user1.get(url)
    content = response.content.decode()
    assert "Профиль" in content
    assert "Выход" in content
    assert "Вход" not in content


# Тест 4: отображение последних постов
@pytest.mark.django_db
def test_latest_posts_displayed(user1, client):
    posts = [Post.objects.create(
        title=f"title {i}", text="...", author=user1
    ) for i in range(3)]
    url = reverse("posts:home")
    response = client.get(url)
    content = response.content.decode()
    for post in posts:
        assert post.title in content


# Тест 5: переход к посту работает
@pytest.mark.django_db
def test_post_link_works(client, user1):
    post = Post.objects.create(
        title="Sample Post",
        text="Content",
        author=user1
    )
    url = reverse('posts:post_detail', args=[post.id])
    response = client.get(url)
    assert response.status_code == 200
    assert post.title in response.content.decode()


# Тест 7: пагинация работает
@pytest.mark.django_db
def test_pagination(client, settings, user1):
    settings.POSTS_PER_PAGE = 3
    for i in range(12):
        Post.objects.create(title=f"title {i}", text="...", author=user1)
    response = client.get(reverse('posts:home') + "?page=2")
    assert response.status_code == 200
    content = response.content.decode()
    assert "&laquo;" in content or "&raquo;" in content
