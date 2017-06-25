# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Recorrido(models.Model):
    nombre = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    endpoint = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
