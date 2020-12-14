from django.db import models
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your models here.
  
class User(models.Model):
  name = models.CharField(max_length=60)
  image_path = models.CharField(max_length=280, null=True)
  email = models.EmailField(max_length=70, blank=True, unique=True)
  password = models.CharField(max_length=20, default='')
  
  def get_absolute_url(self):
    return reverse("myownwork", kwargs={'id': self.id})
  
class Work(models.Model):
  user_id = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
  name = models.CharField(max_length=60)
  text = models.CharField(max_length=280)
  created_at = models.DateTimeField('created_at')
  
  def get_absolute_url(self):
    return reverse("myownwork", kwargs={'id': self.user_id})
  


