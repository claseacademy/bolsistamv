# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

"""

MODELOS DE NEGOCIO O MODELOS DEL SISTEMA QUE DAN ACCESO A LAS TABLAS DE LA BASE DE DATOS

"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    id = models.IntegerField(primary_key = True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    class Meta:
        db_table = User


class Etapas(models.Model):
    id = models.IntegerField(primary_key = True)
    id_user = models.CharField(max_length=10)
    fecha_etapa = models.DateField(auto_now=True)
    tipo_etapa = models.CharField(max_length=1)
    status_etapa = models.CharField(max_length=1)
    class Meta:
        db_table = "etapas"
