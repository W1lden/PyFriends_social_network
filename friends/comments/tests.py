from .models import Comment

def test_add_comment(client, user, post):
    client.force_login(user)
    response = client.post(f"/posts/{post.pk}/", {"text": "Test comment"})
    assert response.status_code == 302
    assert post.comments.last().text == "Test comment"

def test_delete_comment(client, user, comment):
    client.force_login(user)
    response = client.post(f"/comments/delete/{comment.pk}/")
    assert response.status_code == 302
    assert not Comment.objects.filter(pk=comment.pk).exists()

