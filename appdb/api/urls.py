from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name="index"),
    path('users', views.users, name="users"),
    path('posts', views.posts, name="posts"),
    path('meetups', views.meetups, name="meetups"),

]
