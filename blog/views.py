from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post
# Create your views here.

def all_posts(request):
    posts = Post.objects.all().order_by("-created_at")
    context={
        'posts':posts
    }
    return render(request, 'blog/all_posts.html', context)

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    
    context={
        'post':post
    }
    
    return render(request, 'blog/post_detail.html', context)