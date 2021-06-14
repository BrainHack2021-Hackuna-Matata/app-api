from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    title = models.CharField(max_length=50, blank=False, default='')
    usertype = models.BooleanField()
    address = models.CharField(max_length=50, blank=False, default='')
    block = models.CharField(max_length=50, blank=False, default='')
    unit = models.CharField(max_length=50, blank=False, default='')
    postal = models.CharField(max_length=50, blank=False, default='')
    exp = models.IntegerField(blank=False, default=0)


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=50, blank=False, default='')
    items = ArrayField(models.CharField(
        max_length=50, blank=False, default=''))
    imageurl = models.CharField(max_length=200, blank=False, default='')
    coming = ArrayField(models.CharField(
        max_length=50, blank=False, default=''))


class Meetups(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=50, blank=False, default='')
    capacity = models.IntegerField(blank=False, default=0)
    imageurl = models.CharField(max_length=200, blank=False, default='')
    coming = ArrayField(models.CharField(
        max_length=50, blank=False, default=''))
