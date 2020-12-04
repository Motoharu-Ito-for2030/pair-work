from django.db import models

# Create your models here.
  
class User(models.Model):
  name = models.CharField(max_length=60)
  image_path = models.CharField(max_length=280, null=True)
  email = models.EmailField(max_length=70, blank=True, unique=True)
  password = models.CharField(max_length=20, default='')
  
class Work(models.Model):
  name = models.CharField(max_length=60)
  text = models.CharField(max_length=280)
  created_at = models.DateTimeField('created_at')
