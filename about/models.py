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
