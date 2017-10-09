# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    response = "Placeholder to verify rover app creation."
    return render(request, 'rover_index.html', context={'response': response, })
