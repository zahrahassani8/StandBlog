from django.shortcuts import render, get_object_or_404
from .models import *

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    categories = Category.objects.all()
    tips = Tip.objects.all()[:3]
    return render(request, 'blog/article_details.html', context={'article':article, 'tips':tips, 'categories':categories})

