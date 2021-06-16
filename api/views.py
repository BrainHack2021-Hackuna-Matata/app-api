from base64 import b64encode

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import User, Post, Meetups
from .serializers import PostSerializer, UserSerializer, MeetupsSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def login(request):
    allusers = User.objects.all()
    userinfo = JSONParser().parse(request)
    # allusers_s = UserSerializer(allusers, many=True)
    mobile = userinfo['mobile']
    password = userinfo['password']
    for i in allusers:
        if i.mobile == mobile:
            if i.password == password:
                credentials = f"{mobile}:{password}"
                encodedCredentials = str(
                    b64encode(credentials.encode("utf-8")), "utf-8")
                basicauth = f'Basic {encodedCredentials}'
                userser = UserSerializer(i)
                response = JsonResponse(userser.data)
                response.set_cookie('auth', basicauth)
                return response
            else:
                return JsonResponse({'message': 'Wrong password.'})
        # return JsonResponse(allusers_s.data, safe=False, status=status.HTTP_201_CREATED)
        # return JsonResponse({'message': 'fail'})
    return JsonResponse({'message': 'Redirect to register page'})


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        return JsonResponse({'apis': {
            'users': 'Get all users',
            'posts': 'Get all Groupbuy requests',
            'meetups': 'Get all meetup invites',
        }}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def users(request):
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


@api_view(['POST', 'GET'])
def posts(request):
    if request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        allposts = Post.objects.all()
        serialized = PostSerializer(allposts, many=True)
        return JsonResponse(serialized.data, safe=False)


@api_view(['GET', 'DELETE', 'POST'])
def onepost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        serialized = PostSerializer(post)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'DELETE':
        post.delete()
        return JsonResponse({'success': 'Post was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        post.fulfilled = data['fulfilled']
        post.accepted = data['accepted']
        post.coming = data['coming']
        post.save()
        return JsonResponse({'success': 'Post was updated successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def meetups(request):
    if request.method == 'POST':
        meetups_data = JSONParser().parse(request)
        meetups_serializer = MeetupsSerializer(data=meetups_data)
        if meetups_serializer.is_valid():
            meetups_serializer.save()
            return JsonResponse(meetups_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(meetups_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        allmeetups = Meetups.objects.all()
        serialized = MeetupsSerializer(allmeetups, many=True)
        return JsonResponse(serialized.data, safe=False)


@api_view(['GET', 'DELETE', 'POST'])
def onemeetup(request, pk):
    meetup = Meetups.objects.get(id=pk)
    if request.method == 'GET':
        serialized = MeetupsSerializer(meetup)
        return JsonResponse(serialized.data, safe=False)
    if request.method == 'DELETE':
        meetup.delete()
        return JsonResponse({'success': 'Meetup was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        meetup.coming = data['coming']
        meetup.save()
        return JsonResponse({'success': 'Meetup was updated successfully.'}, status=status.HTTP_204_NO_CONTENT)
