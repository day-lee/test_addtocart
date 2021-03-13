from django.contrib import admin
from .models import Post, Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
#This will allow our blog post entries to be accessible from the admin area
