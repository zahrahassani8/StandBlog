from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    tips = Tip.objects.all()[:3]
    categories = Category.objects.all()
    
    return render(request, 'blog/article_details.html', context={'article':article, 'tips':tips, 'categories':categories})


def post_list(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', context={'posts':objects_list, 'categories':categories})