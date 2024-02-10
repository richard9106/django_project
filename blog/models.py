"""import model to create user models"""

from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.


class Post(models.Model):
    """create a model user"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    content = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        """meta class"""
        ordering = ["-create_on"]

    def __str__(self):
        """Methods """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """create a model for manage the comments"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comment"
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    body = models.TextField()
    Approved = models.BooleanField(default=False)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """meta class"""
        ordering = ["-create_on"]

    def __str__(self):
        """Methods """
        return f"Comment {self.body} | written by {self.author}"
