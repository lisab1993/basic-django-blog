from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title