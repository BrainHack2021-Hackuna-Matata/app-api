from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, default='')
    mobile = models.CharField(max_length=50, blank=False, default='')
    password = models.CharField(max_length=50, blank=False, default='')
    usertype = models.BooleanField()
    block = models.CharField(max_length=50, blank=False, default='')
    postal = models.CharField(max_length=50, blank=False, default='')
    unit = models.CharField(max_length=50, blank=False, default='')
    lat = models.DecimalField(decimal_places=5, max_digits=8, default=0)
    long = models.DecimalField(decimal_places=5, max_digits=8, default=0)
    exp = models.IntegerField(blank=False, default=0)

    class Meta:
        ordering = ['id']


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=50, blank=False, default='')
    items = ArrayField(models.CharField(
        max_length=50, blank=False, default=''))
    imageurl = models.CharField(max_length=200, blank=False, default='')
    coming = ArrayField(models.CharField(
        max_length=50, blank=False, default=''))
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    fulfilled = models.BooleanField()
    accepted = models.BooleanField()
    lat = models.DecimalField(decimal_places=5, max_digits=8, default=0)
    long = models.DecimalField(decimal_places=5, max_digits=8, default=0)
    unit = models.CharField(max_length=50, blank=False, default='')

    class Meta:
        ordering = ['-created']


class Meetups(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, default='')
    location = models.CharField(max_length=50, blank=False, default='')
    capacity = models.IntegerField(blank=False, default=0)
    coming = ArrayField(models.CharField(
        max_length=50, blank=False, default=''))
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    hostname = models.CharField(max_length=50, blank=False, default='')

    class Meta:
        ordering = ['-created']
