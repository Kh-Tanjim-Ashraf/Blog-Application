from django.shortcuts import render
from .models import Post

def postList (request):
    posts = Post.objects.all().order_by('-date')
    context = {
        'posts' : posts
    }
    return render(request, 'post/post-list.html', context)
