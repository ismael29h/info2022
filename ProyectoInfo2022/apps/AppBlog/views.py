from django.shortcuts import redirect, render

from .models import Post
from .forms import CommentForm
# Create your views here.
 

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'posts/index.html', {'posts':posts})

def banners(request):
    posts = Post.objects.all()

    return render(request, 'posts/blog.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        com = {
            'name': request.user.id,
            'body': request.POST['comment'],
            'post': request.POST['post']
        }

        form = CommentForm(com)

        if form.is_valid():
            form.save()

            return redirect('posts:post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'posts/detail.html', {'post': post, 'form': form})
