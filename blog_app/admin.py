from django.contrib import admin
from blog_app.models import *
# Register your models here.
# admin.site.register(Post)
admin.site.register((Post,BlogComments))