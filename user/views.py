from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def registerUser (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'user/user-add.html', context)


def loginUser (request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # print("form:", form.__dir__())
        if form.is_valid():
            print("form:", form.get_user())
            login(request, form.get_user())
            return redirect('homePage')
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, 'user/user-login.html', context)


def logoutUser (request):
    if request.method == 'POST':
        logout(request)
        return redirect('homePage')
