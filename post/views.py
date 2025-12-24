from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def postList (request):
    posts = Post.objects.all().order_by('-date')
    context = {
        'posts' : posts
    }
    return render(request, 'post/post-list.html', context)

def postDetail (request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'post/post-detail.html', context)

@login_required(login_url='UserApp:loginUser')
def postAdd (request):
    return render(request, 'post/post-add.html')
