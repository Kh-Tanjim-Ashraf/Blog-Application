from django.shortcuts import render

def postList (request):
    return render (request, 'post/post-list.html')
