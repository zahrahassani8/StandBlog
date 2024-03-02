from django.shortcuts import render
from blog.models import *

def home(request):
    articles = Article.objects.all()
    posts = Post.objects.all()
    return render(request, 'home/home.html', context={'articles':articles, 'posts':posts})
