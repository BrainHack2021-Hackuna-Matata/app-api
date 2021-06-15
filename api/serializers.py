from rest_framework import serializers
from .models import User, Post, Meetups


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
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
            'id',
            'title',
            'description',
            'location',
            'items',
            'imageurl',
            'coming',
            'created',
        )


class MeetupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetups
        fields = (
            'id',
            'title',
            'description',
            'location',
            'capacity',
            'imageurl',
            'coming',
            'created',
        )
