import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_all_posts_accessible(client):
    url = reverse('posts:all_posts')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_accessible(post_user1, client):
    url = reverse('posts:post_detail', args=[post_user1.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_unaccessible(post_user1, client):
    url = reverse('posts:post_create')
    response = client.get(url)
    assert response.status_code == 302  # редирект в логин


@pytest.mark.django_db
def test_delete_unaccessible(post_user1, client):
    url = reverse('posts:post_delete', args=[post_user1.id])
    response = client.get(url)
    assert response.status_code == 302  # редирект в логин


@pytest.mark.django_db
def test_edit_unaccessible(post_user1, client):
    url = reverse('posts:post_edit', args=[post_user1.id])
    response = client.get(url)
    assert response.status_code == 302  # редирект в логин
