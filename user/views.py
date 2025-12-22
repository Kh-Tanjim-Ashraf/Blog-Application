from django.shortcuts import render


def registerUser (request):
    return render(request, 'user/user-add.html')
