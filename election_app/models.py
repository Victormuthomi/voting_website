from django.db import models

# Create your models here.

class Election(models.Model):
    """A elction to be held"""
    name = models.CharField(max_length=50)
    date = models.DateField()
    details = models.TextField()
    
