# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import HttpResponse, redirect, render

# rover imports
from .rover import *


def index(request):
    return render(request, 'rover_index.html', context=None)


def move(request, direction):
    move_rover(direction)
    print direction
    data = {
        'direction': direction,
    }
    return HttpResponse(json.dumps(data))
