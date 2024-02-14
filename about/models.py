"""import model to create user models"""

from django.db import models

# Create your models here.


class About(models.Model):
    """create a model for about content"""
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    update_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        """retur the title"""
        return self.title


class CollaborateRequest(models.Model):
    """model for the collaborate form"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
