from django.shortcuts import redirect, render

from .models import Post
# Create your views here.
 

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'posts/index.html', {'posts':posts})

def banners(request):
    posts = Post.objects.all()

    return render(request, 'posts/blog.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'posts/detail.html', {'post': post})
