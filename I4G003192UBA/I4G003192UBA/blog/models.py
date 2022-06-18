from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Text = models.CharField(max_length=255, unique=True)
    Author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['created_on']


def __str__(self):
    return self.Title
