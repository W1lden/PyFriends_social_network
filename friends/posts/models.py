from django.db import models

from .constants import max_length_author, max_length_text, max_length_title


class Post(models.Model):
    title = models.CharField(max_length=max_length_title)
    text = models.TextField(max_length=max_length_text)
    author = models.CharField(max_length=max_length_author)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
