from django.shortcuts import render
from blog.models import *

def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    tips = Tip.objects.all()[:3]
    return render(request, 'home/home.html', context={'articles':articles, 'posts':posts, 'tips':tips, 'categories':categories})
