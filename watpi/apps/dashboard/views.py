# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    response = "Placeholder to verify dashboard app creation."
    return HttpResponse(response)
