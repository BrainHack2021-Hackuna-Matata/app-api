from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import User, Post, Meetups
from .serializers import PostSerializer, UserSerializer, MeetupsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    return JsonResponse({'message': 'Hello World'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
def users(request):
    api = User.objects.all()
    stuff = UserSerializer(api, many=True)
    return JsonResponse(stuff.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def posts(request):
    api = Post.objects.all()
    stuff = PostSerializer(api, many=True)
    return JsonResponse(stuff.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def meetups(request):
    api = Meetups.objects.all()
    stuff = MeetupsSerializer(api, many=True)
    return JsonResponse(stuff.data, safe=False)
