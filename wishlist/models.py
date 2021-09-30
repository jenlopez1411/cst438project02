from django.db import models

# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
