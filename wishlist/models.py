from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
class Items(models.Model):
     item_id = models.AutoField(primary_key=True)
     user_id = models.IntegerField
     list_id = models.IntegerField
     name = models.CharField(max_length=200)
     url = models.URLField
     description = models.TextField
     picture_url = models.URLField
     user_priority = models.CharField
     slug = models.SlugField(unique=True)

class List(models.Model):
    listId = models.AutoField(primary_key=True)
    userId = models.IntegerField
    list_name =  models.CharField(max_length=50)
    