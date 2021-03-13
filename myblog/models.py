from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self): #url name
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')




# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Hello Blog') #for title on each article page
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #if we delete the user, blog post under that name will be deleted altogher. (Cascading)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True) #automatically assign date
    category = models.CharField(max_length=255, default='coding') #default bc we adds it after db built and has old posts


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    #on our admin page, object will be shown with recognizeable text.


    def get_absolute_url(self): #url name
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')