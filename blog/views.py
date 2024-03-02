from django.shortcuts import render
from .models import *

def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/article_details.html', context={'article':article})

