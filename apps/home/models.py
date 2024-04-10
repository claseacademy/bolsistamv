# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

"""

MODELOS DE NEGOCIO O MODELOS DEL SISTEMA QUE DAN ACCESO A LAS TABLAS DE LA BASE DE DATOS

"""

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

'''
username=request.POST["username"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    email=request.POST["email"],
                    telefono=request.POST["telefono"],
                    id_tipo_usuario=request.POST["id_tipo_usuario"],
                    documento=request.POST["documento"],
                    sexo=request.POST["sexo"],
                    is_staff=0,
                    is_active=1,
                    is_superuser=0
'''

class Usuario(models.Model):
    id = models.IntegerField(primary_key = True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_staff = models.CharField(max_length=100)
    is_active = models.CharField(max_length=100)
    is_superuser = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now=True)
    class Meta:
        managed = False
        db_table = "auth_user"


class UsuarioExtra(models.Model):
    id = models.IntegerField(primary_key = True)
    id_user = models.IntegerField()
    telefono = models.CharField(max_length=100)
    id_tipo_usuario = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    class Meta:
        db_table = "user_extra"



class Etapas(models.Model):
    id = models.IntegerField(primary_key = True)
    id_user = models.IntegerField()
    fecha_etapa = models.DateField(auto_now=True)
    fecha_etapa = models.DateField(auto_now=True)
    tipo_etapa = models.CharField(max_length=1)
    status_etapa = models.IntegerField()
    class Meta:
        db_table = "etapas"


class CapitalInversion(models.Model):
    id = models.IntegerField(primary_key = True)
    id_user = models.IntegerField()
    tipo_inversion = models.IntegerField()
    fecha_inversion = models.DateField()
    fecha_retorno_inversion = models.DateField()
    moneda_inversion = models.CharField(max_length=50)
    monto_inversion = models.DecimalField(max_digits=10, decimal_places=2)
    interes_inversion = models.DecimalField(max_digits=10, decimal_places=2)
    status_inversion = models.IntegerField(default=1)
    class Meta:
        db_table = "capital_inversion"

class TipoInversion(models.Model):
    id = models.IntegerField(primary_key = True)
    name_tipo_inversion = models.CharField(max_length=250)
    class Meta:
        db_table = "tipo_inversion"


class CapitalOperaciones(models.Model):
    id = models.IntegerField(primary_key = True)
    id_user = models.IntegerField()
    id_capital_inversion = models.IntegerField()
    fecha_operacion = models.DateField()
    monto_operacion = models.DecimalField(max_digits=10, decimal_places=2)
    status_operacion = models.IntegerField()
    class Meta:
        db_table = "capital_operaciones"


class CapitalPrestamos(models.Model):
    id = models.IntegerField(primary_key = True)
    id_user = models.IntegerField()
    id_etapas = models.IntegerField()
    tipo_prestamo = models.IntegerField()
    fecha_prestamo = models.DateField()
    tiempo_prestamo = models.IntegerField()
    taza_interes_prestamo = models.DecimalField(max_digits=10, decimal_places=2)
    monto_solicitado_prestamo = models.DecimalField(max_digits=10, decimal_places=2)
    firma_prestamo = models.IntegerField()
    status_prestamo = models.IntegerField()
    class Meta:
        db_table = "capital_prestamos"
