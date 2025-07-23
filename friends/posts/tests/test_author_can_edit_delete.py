import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_author_can_edit_post(post_user1, authenticated_user1, client):
    url = reverse('posts:post_edit', args=[post_user1.id])
    response = authenticated_user1.get(url)
    assert response.status_code == 200  # успешный доступ


@pytest.mark.django_db
def test_author_can_delete_post(post_user1, authenticated_user1, client):
    url = reverse('posts:post_delete', args=[post_user1.id])
    response = authenticated_user1.get(url)
    assert response.status_code == 302  # редирект после удаления
