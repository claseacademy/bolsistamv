# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from apps.home.models import Usuario
from apps.home.models import Etapas

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapas
        fields = "__all__"