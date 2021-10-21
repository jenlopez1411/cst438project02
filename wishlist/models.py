from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
        
    class Meta:
        managed = True
        db_table = 'User'
    

class Items(models.Model):
     item_id = models.AutoField(primary_key=True)
     user_id = models.IntegerField()
     list_id = models.IntegerField()
     name = models.CharField(max_length=200)
     url = models.URLField()
     description = models.TextField()
     picture_url = models.URLField()
     user_priority = models.CharField(max_length=1000)
     slug = models.SlugField(unique=True)

     class Meta:
        managed = True
        db_table = 'Item'
    

class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    list_name =  models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        managed = True
        db_table = 'List'

class AdminUsers(models.Model): 
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'AdminUsers'