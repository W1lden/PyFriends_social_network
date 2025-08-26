import pytest
from comments.models import Comment
from django.urls import reverse


@pytest.mark.django_db
def test_anonymous_cannot_add_comment(client, post):
    response = client.post(reverse("comments:post_detail", args=[post.pk]), {
        "text": "Test comment"
    })
    assert Comment.objects.count() == 0
    assert response.status_code == 200  #


@pytest.mark.django_db
def test_authenticated_user_can_add_comment(
    client,
    user,
    post,
    authenticated_client
):
    response = authenticated_client.post(
        reverse("comments:post_detail", args=[post.pk]),
        {"text": "Valid comment"})
    assert response.status_code == 302
    assert Comment.objects.count() == 1
    comment = Comment.objects.first()
    assert comment.author == user
    assert comment.post == post


@pytest.mark.django_db
def test_author_can_delete_own_comment(authenticated_client, comment):
    url = reverse("comments:comment_delete", args=[comment.pk])
    response = authenticated_client.post(url)
    assert response.status_code == 302
    assert Comment.objects.count() == 0


@pytest.mark.django_db
def test_other_user_cannot_delete_comment(client, other_user, comment):
    client.force_login(other_user)
    url = reverse("comments:comment_delete", args=[comment.pk])
    response = client.post(url)
    assert response.status_code == 302
    assert Comment.objects.count() == 1


@pytest.mark.django_db
def test_admin_can_delete_any_comment(admin_client, comment):
    url = reverse("comments:comment_delete", args=[comment.pk])
    response = admin_client.post(url)
    assert response.status_code == 302
    assert Comment.objects.count() == 0
