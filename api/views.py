from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import User, Post, Meetups
from .serializers import PostSerializer, UserSerializer, MeetupsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    return JsonResponse({'apis': {
        'users': 'Get all users',
        'posts': 'Get all Groupbuy requests',
        'meetups': 'Get all meetup invites',
    }}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        user = User.objects.all()
        serialized = UserSerializer(user, many=True)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def oneuser(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'GET':
        serialized = UserSerializer(user)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'success': 'User was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serialized = PostSerializer(post, many=True)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def onepost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        serialized = PostSerializer(post)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'DELETE':
        post.delete()
        return JsonResponse({'success': 'Post was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def meetups(request):
    if request.method == 'GET':
        meetup = Meetups.objects.all()
        serialized = MeetupsSerializer(meetup, many=True)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'POST':
        meetups_data = JSONParser().parse(request)
        meetups_serializer = MeetupsSerializer(data=meetups_data)
        if meetups_serializer.is_valid():
            meetups_serializer.save()
            return JsonResponse(meetups_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(meetups_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def onemeetup(request, pk):
    meetup = Meetups.objects.get(id=pk)
    if request.method == 'GET':
        serialized = MeetupsSerializer(meetup)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'DELETE':
        meetup.delete()
        return JsonResponse({'success': 'Meetup was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
