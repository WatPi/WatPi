# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    if request.user.is_authenticated:
        response = "Placeholder to verify dashboard app creation."
        return render(request, 'dashboard_index.html', context={'response': response, })
    else:
        return redirect('/login')
