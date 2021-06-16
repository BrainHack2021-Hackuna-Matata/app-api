from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name="index"),
    path('users', views.users, name="users"),
    url(r'^users/(?P<pk>[0-9]+)$', views.oneuser),
    path('posts', views.posts, name="posts"),
    url(r'^posts/(?P<pk>[0-9]+)$', views.onepost),
    path('meetups', views.meetups, name="meetups"),
    url(r'^meetups/(?P<pk>[0-9]+)$', views.onemeetup),
    path('login', views.login, name="login"),

    url(r'^posts/user/(?P<pk>[0-9]+)$', views.userPosts),

]
