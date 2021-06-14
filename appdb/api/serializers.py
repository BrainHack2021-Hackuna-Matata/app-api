from rest_framework import serializers
from .models import User, Post, Meetups


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'title',
            'usertype',
            'address',
            'block',
            'unit',
            'postal',
            'exp',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'location',
            'items',
            'imageurl',
            'coming',
        )


class MeetupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetups
        fields = (
            'title',
            'description',
            'location',
            'capacity',
            'imageurl',
            'coming',
        )
