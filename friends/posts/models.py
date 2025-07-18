# comments/models.py (временно)
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):  # временная заглушка
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
