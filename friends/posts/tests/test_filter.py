import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_filter(client, user1):
    url = reverse('posts:all_posts') + f'?author={user1.username}'
    response = client.get(url)
    content = response.content.decode()

    assert 'Alex' in content
    assert 'Jack' not in content
