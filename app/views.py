from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SigninForm, SignupForm


def index(request):
    return render(request, "app/index.html")

def signin(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'site-admin':
            return redirect('/courses/admin_dashboard/')
        return redirect('/courses')
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            if user.groups.all()[0].name == 'site-admin':
                return redirect('/courses/admin_dashboard/')
            return redirect('/courses/')
    else:
        form = SigninForm()
    return render(request, 'app/signin.html', {'form':form})

def signup(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'site-admin':
            return redirect('/courses/admin_dashboard/')
        return redirect('/courses')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, "app/signup.html", {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')
