# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm, ChangePassForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import logging
logging.basicConfig(level=logging.INFO)

def index(request):
    if request.method != "POST":
        if request.user.is_authenticated:
            username = request.user.username
            form = ChangePassForm(initial={'username': username})
            context = {
                "title": "Change Password",
                "form": form,
            }
            return render(request, 'login/login.html', context)
        else:
            if len(User.objects.all()) == 0:
                user = User.objects.create_superuser("admin","nothing@null.nil","password")
            form = LoginForm()
            context = {
                "title": "Welcome to WatPi",
                "form": form,
            }
            return render(request, 'login/login.html', context)
    else:
        if request.user.is_authenticated():
            user = User.objects.get(id=request.user.id)
            user.password
        else:
            post = request.POST
            form = LoginForm(post)
            if form.is_valid():
                logging.info(form.cleaned_data)
                login(request, form.cleaned_data['user'])
                return redirect('/dashboard')
            context = {
                "title": "Welcome to WatPi",
                "form": form,
            }
            return render(request, 'login/login.html', context)

def logmeout(request):
    logout(request)
    return redirect("/")
