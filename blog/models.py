from django.db import models
from django.utils.text import slugify
from django.urls import reverse
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
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])



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
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def get_absolute_url(self):
        return reverse('home:home', args=[self.slug])


class Tip(models.Model):
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.text
