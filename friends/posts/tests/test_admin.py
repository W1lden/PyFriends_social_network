import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_admin_can_delete_post1(post_user1, authenticated_admin, client):
    url = reverse('posts:post_delete', args=[post_user1.id])
    response = authenticated_admin.get(url)
    assert response.status_code == 302  # редирект после удаления


@pytest.mark.django_db
def test_admin_can_delete_post2(post_user2, authenticated_admin, client):
    url = reverse('posts:post_delete', args=[post_user2.id])
    response = authenticated_admin.get(url)
    assert response.status_code == 302  # редирект после удаления
