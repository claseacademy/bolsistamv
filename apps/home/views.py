# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

"""

CONTROLADOR PRINCIPAL DEL SISTEMA

"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from apps.home.forms import UsuarioForm
#from apps.home.models import Usuario
from django.contrib.auth.models import User

from apps.home.models import Etapas
from apps.home.forms import EtapaForm

from datetime import datetime



@login_required(login_url="/login/")
def index(request):

    etapa = Etapas.objects.filter(id_user=request.user.id)
    html_template = loader.get_template('home/index.html')
    context = {
        'segment': 'index',
        'etapa': etapa,
    }
    return HttpResponse(html_template.render(context, request))


def usuarios(request):

    usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/usuarios_etapas.html')
    context = {
        'usuario': usuario,
    }
    return HttpResponse(template.render(context, request))

def etapa(request):

    etapa = Etapas.objects.all()
    template = loader.get_template('home/index_etapa.html')
    context = {
        'etapa': etapa,
    }
    return HttpResponse(template.render(context, request))

def etapa_id(request, id):

    etapa = Etapas.objects.filter(id_user=id)
    template = loader.get_template('home/index_etapa.html')
    context = {
        'etapa': etapa,
    }

    return HttpResponse(template.render(context, request))

def edit_status_etapa_id(request, id, idu):

    status_etapa = request.POST['status_etapa']
    etapa = Etapas.objects.get(id=id)
    #etapa.fecha_etapa = datetime.now()  # obtiene la fecha actual
    etapa.status_etapa = status_etapa
    etapa.save()
    #template = loader.get_template('home/index_etapa.html')
    #etapa = Etapas.objects.filter(id_user=idu)
    #return redirect(f"/etapa_id/{idu}")
    return redirect(f"/usuarios/")
    #return HttpResponse(template.render(context, request))

def edit_status_etapa(request, id):

    status_etapa = request.POST['status_etapa']
    etapa = Etapas.objects.get(id=id)
    etapa.status_etapa = status_etapa
    etapa.save()
    template = loader.get_template('home/index_etapa.html')
    etapa = Etapas.objects.all()
    context = {
        'etapa': etapa,
    }
    return redirect("/usuarios")
    #return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def perfil(request, id):

    user = User.objects.get(id=id)
    form = UsuarioForm(request.POST, instance = user)
    t = loader.get_template("home/user.html")
    c = {"foo": user}
    if form.is_valid():
        form.save()

    return HttpResponse(t.render(c, request))

