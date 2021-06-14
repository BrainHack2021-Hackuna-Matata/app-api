from django.contrib import admin

# Register your models here.
from .models import User, Post, Meetups

admin.site.site_header = "Hackuna Matata"
admin.site.site_title = "Hackuna Matata Admin Area"
admin.site.index_title = "Welcome to Admin Site"

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Meetups)
