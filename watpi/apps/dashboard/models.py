# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Photo(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

