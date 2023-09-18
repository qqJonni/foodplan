from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserLkForm
from django.contrib import auth
from django.urls import reverse
from users.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:lk'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Foodplan 2021 - Меню на неделю FOODPLAN',
        'form': form
    }
    return render(request, 'users/login.html', context)


def lk(request):
    if request.method == 'POST':
        form = UserLkForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:lk'))
    else:
        form = UserLkForm(instance=request.user)
    context = {
        'title': 'Foodplan 2021 - Меню на неделю FOODPLAN',
        'form': form,
        'username': request.user.username
    }
    return render(request, 'users/lk.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Foodplan 2021 - Меню на неделю FOODPLAN',
        'form': form
    }
    return render(request, 'users/registration.html', context)
