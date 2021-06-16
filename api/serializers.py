from rest_framework import serializers
from .models import User, Post, Meetups


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'mobile',
            'password',
            'usertype',
            'block',
            'postal',
            'unit',
            'lat',
            'long',
            'exp',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'location',
            'items',
            'imageurl',
            'coming',
            'owner',
            'created',
            'due',
            'fulfilled',
            'accepted',
            'lat',
            'long',
            'unit',
        )


class MeetupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetups
        fields = (
            'id',
            'title',
            'location',
            'capacity',
            'coming',
            'owner',
            'created',
            'due',
            'hostname',
        )
