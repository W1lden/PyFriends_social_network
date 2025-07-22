import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_not_author_cant_edit(post_user1, authenticated_user2, client):
    url = reverse('posts:post_edit', args=[post_user1.id])
    response = authenticated_user2.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_not_author_cant_delete(post_user1, authenticated_user2, client):
    url = reverse('posts:post_delete', args=[post_user1.id])
    response = authenticated_user2.get(url)
    assert response.status_code == 403
