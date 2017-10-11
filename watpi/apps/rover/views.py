# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import HttpResponse, redirect, render

# rover imports
from .rover import *


def index(request):
    return render(request, 'index.html', context=None)


def move(request, direction):
    move_rover(direction)
    print direction
    data = {
        'direction': direction,
    }
    return HttpResponse(json.dumps(data))

def stop(request):
    stop_rover()
    print 'stopped'
    data = {
        'direction': 'stopped',
    }
    return HttpResponse(json.dumps(data))
