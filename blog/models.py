from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    category = models.ManyToManyField(Category, related_name="articles")
    body = models.TextField()
    image = models.ImageField(upload_to="article_image")
    slug = models.SlugField(null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-created',)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    category = models.ManyToManyField(Category, related_name="posts")
    body = models.TextField()
    image = models.ImageField(null=True, upload_to="post_image")
    slug = models.SlugField(null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.title