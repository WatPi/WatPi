# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm, ChangePassForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import logging

logging.basicConfig(level=logging.INFO)

def index(request):
    if request.method != "POST":
        if request.user.is_authenticated:
            username = request.user.username
            form = ChangePassForm(initial={'username': username})
            context = {
                "title": "WatPi | Change Password",
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
            post = request.POST
            form = ChangePassForm(post)
            if form.is_valid():
                logging.info(form.cleaned_data)
                user = User.objects.get(username=request.user.username)
                user.username = form.cleaned_data['new_login']
                user.set_password(form.cleaned_data['new_pass'])
                user.save()
                logging.info(user)
                return redirect('/dashboard')
            context = {
                "title": "WatPi Admin",
                "form": form,
            }
            return render(request, 'login/login.html', context)


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
