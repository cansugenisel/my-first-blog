from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(yaratilma_tarihi__lte=timezone.now()).order_by('yaratilma_tarihi')
    return render(request, 'blog/post_list.html',{'posts': posts})
