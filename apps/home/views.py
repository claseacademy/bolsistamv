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
from apps.home.models import Usuario, UsuarioExtra, CapitalInversion, CapitalOperaciones, CapitalPrestamos, TipoInversion, TipoPrestamo
from django.contrib.auth.models import User, Group

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


# USUARIOS CRUD

@login_required(login_url="/login/")
def usuarios(request):

    usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/usuarios_etapas.html')
    context = {
        'usuario': usuario,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def create_user(request):

    grupos = Group.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/create_user.html')
    context = {
        #'usuario': usuario,
        'grupos': grupos,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def store_user(request):

    if request.method == "POST":

        verificando = Usuario.objects.filter(username=request.POST["username"]).exists()
        verificando2 = Usuario.objects.filter(email=request.POST["email"]).exists()
        if verificando == False and verificando2 == False:
            try:
                Usuario.objects.create(
                    password="pbkdf2_sha256$260000$6BQKaYZbawBeOJaQR5hltH$qKV/agmE8w3kS/BETzkS62L/DmzEaRAsipEo122736A=",
                    username=request.POST["username"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    email=request.POST["email"],
                    is_staff=0,
                    is_active=1,
                    is_superuser=0
                )
                id_user = Usuario.objects.values('id').last()
                UsuarioExtra.objects.create(
                    id_user=id_user['id'],
                    telefono=request.POST["telefono"],
                    id_tipo_usuario=request.POST["id_tipo_usuario"],
                    documento=request.POST["documento"],
                    sexo=request.POST["sexo"]
                )
                for x in range(5):
                    x+=1
                    Etapas.objects.create(id_user=id_user['id'], tipo_etapa=x, status_etapa=0)

                return redirect("/usuarios")
            except:
                pass

        else:
            grupos = Group.objects.all().order_by('id').values()
            #usuario = User.objects.all().exclude(id=2).exclude(id=3)
            template = loader.get_template('home/create_user.html')
            context = {
                #'usuario': usuario,
                'grupos': grupos,
                'alert': "El correo o el usuario ya existe!",
            }
            return HttpResponse(template.render(context, request))

    else:
        return redirect("/usuarios")


@login_required(login_url="/login/")
def add_info_adicional_user(request, id):

    grupos = Group.objects.all().order_by('id').values()
    usuario = Usuario.objects.filter(id=id)
    verificando = UsuarioExtra.objects.filter(id_user=id).exists()
    if verificando:
        usuarioextra = UsuarioExtra.objects.filter(id_user=id)
    #print(usuarioextra[0].telefono)
    template = loader.get_template('home/add_info_adicional_user.html')
    context = {
        'usuario': usuario[0].username,
        'usuarioextra': usuarioextra,
        'id_user': id,
        'grupos': grupos,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def add_info_adicional_store_user(request, id):

    if request.method == "POST":

        verificando = UsuarioExtra.objects.filter(id_user=id).exists()
        if verificando == False:
            try:
                UsuarioExtra.objects.create(
                    id_user=id,
                    telefono=request.POST["telefono"],
                    id_tipo_usuario=request.POST["id_tipo_usuario"],
                    documento=request.POST["documento"],
                    sexo=request.POST["sexo"]
                )

                return redirect("/usuarios")
            except:
                pass

        else:

            usuarioextra = UsuarioExtra.objects.get(id_user=id)
            usuarioextra.telefono = request.POST["telefono"]
            usuarioextra.id_tipo_usuario = request.POST["id_tipo_usuario"]
            usuarioextra.documento = request.POST["documento"]
            usuarioextra.sexo = request.POST["sexo"]
            usuarioextra.save()

            verificando = UsuarioExtra.objects.filter(id_user=id).exists()
            if verificando:
                usuarioextra = UsuarioExtra.objects.filter(id_user=id)


            grupos = Group.objects.all().order_by('id').values()
            usuario = Usuario.objects.filter(id=id)
            template = loader.get_template('home/add_info_adicional_user.html')
            context = {
                'usuario': usuario[0].username,
                'usuarioextra': usuarioextra,
                'grupos': grupos,
                'alert': "Información del usario ha sido actualizada!",
            }
            return HttpResponse(template.render(context, request))

    else:
        return redirect("/usuarios")



# USUARIOS CRUD

# CAPITAL DE INVERSION

# modelo CapitalInversion
# form_capital_inversion.html,

@login_required(login_url="/login/")
def table_capital_inversion(request):

    capitalinversion = CapitalInversion.objects.all().order_by('id').values()
    tipoinversion = TipoInversion.objects.all().order_by('id').values()
    usuario = Usuario.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/table_capital_inversion.html')
    context = {
        'capitalinversion': capitalinversion,
        'tipoinversion': tipoinversion,
        'usuario': usuario,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_capital_inversion(request):

    usuarioextra = UsuarioExtra.objects.filter(id_tipo_usuario=1).order_by('id')
    usuario = []
    for x in usuarioextra:
        e = Usuario.objects.filter(id=x.id_user)
        usuario.append({'id':x.id_user, 'username':e[0].username})

    #for x in range(len(usuario)):
    #    print(usuario[x]['id'])
    #    print(usuario[x]['username'])

    tipoinversion = TipoInversion.objects.all().order_by('id').values()

    template = loader.get_template('home/form_capital_inversion.html')
    context = {
        'usuario': usuario,
        'tipoinversion': tipoinversion,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_capital_inversion_store(request):

    if request.method == "POST":

        verificando = CapitalInversion.objects.filter(tipo_inversion=request.POST["tipo_inversion"]).exists()
        if verificando == False:
            try:
                CapitalInversion.objects.create(
                    id_user=request.POST["id_user"],
                    tipo_inversion=request.POST["tipo_inversion"],
                    fecha_inversion=request.POST["fecha_inversion"],
                    fecha_retorno_inversion=request.POST["fecha_retorno_inversion"],
                    moneda_inversion=request.POST["moneda_inversion"],
                    monto_inversion=request.POST["monto_inversion"],
                    interes_inversion=request.POST["interes_inversion"],
                    status_inversion=1
                )
                return redirect("/table_capital_inversion")
            except:
                pass

    return redirect("/table_capital_inversion")


@login_required(login_url="/login/")
def form_capital_inversion_edit(request, id):

    capitalinversion = CapitalInversion.objects.filter(id=id)
    usuarioextra = UsuarioExtra.objects.filter(id_tipo_usuario=1).order_by('id')
    usuario = []
    for x in usuarioextra:
        e = Usuario.objects.filter(id=x.id_user)
        usuario.append({'id':x.id_user, 'username':e[0].username})

    tipoinversion = TipoInversion.objects.all().order_by('id')

    template = loader.get_template('home/form_capital_inversion_edit.html')
    context = {
        'capitalinversion': capitalinversion,
        'usuario': usuario,
        'tipoinversion': tipoinversion,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def table_tipo_inversion(request):

    tipoinversion = TipoInversion.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/table_tipo_inversion.html')
    context = {
        'tipoinversion': tipoinversion,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def form_tipo_inversion(request):

    #tipoinversion = TipoInversion.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/form_tipo_inversion.html')
    context = {
        #'tipoinversion': tipoinversion,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_tipo_inversion_store(request):

    if request.method == "POST":

        verificando = TipoInversion.objects.filter(name_tipo_inversion=request.POST["name_tipo_inversion"]).exists()
        if verificando == False:
            try:
                TipoInversion.objects.create(
                    name_tipo_inversion=request.POST["name_tipo_inversion"]
                )
                return redirect("/table_tipo_inversion")
            except:
                pass

    return redirect("/table_tipo_inversion")

# CAPITAL DE INVERSION

# CAPITAL DE OPERACIONES

# modelo CapitalInversion
# form_capital_inversion.html,

@login_required(login_url="/login/")
def table_capital_operaciones(request):

    capitalinversion = CapitalInversion.objects.all().order_by('id').values()
    capitaloperaciones = CapitalOperaciones.objects.all().order_by('id').values()
    usuarioextra = UsuarioExtra.objects.filter(id_tipo_usuario=1).order_by('id')
    usuario = []
    for x in usuarioextra:
        e = Usuario.objects.filter(id=x.id_user)
        usuario.append({'id':x.id_user, 'username':e[0].username})
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/table_capital_operaciones.html')
    context = {
        'capitalinversion': capitalinversion,
        'capitaloperaciones': capitaloperaciones,
        'usuario': usuario,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_capital_operaciones(request):

    capitalinversion = CapitalInversion.objects.all().order_by('id').values()
    usuarioextra = UsuarioExtra.objects.filter(id_tipo_usuario=1).order_by('id')
    usuario = []
    for x in usuarioextra:
        e = Usuario.objects.filter(id=x.id_user)
        usuario.append({'id':x.id_user, 'username':e[0].username})
    #grupos = Group.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/form_capital_operaciones.html')
    context = {
        'capitalinversion': capitalinversion,
        'usuario': usuario,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_capital_operaciones_store(request):

    if request.method == "POST":

        try:
            CapitalOperaciones.objects.create(
                id_user=1,
                id_capital_inversion=1,
                fecha_operacion=request.POST["fecha_operacion"],
                monto_operacion=request.POST["monto_operacion"],
                status_operacion=1
            )
            return redirect("/table_capital_operaciones")
        except:
            pass

    return redirect("/table_capital_operaciones")

    #grupos = Group.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/form_capital_inversion.html')
    context = {
        'alert': "",
    }
    return HttpResponse(template.render(context, request))



# CAPITAL DE OPERACIONES

# CAPITAL DE PRESTAMOS

# modelo CapitalInversion
# form_capital_inversion.html,

@login_required(login_url="/login/")
def table_capital_prestamos(request):

    capitalprestamos = CapitalPrestamos.objects.all().order_by('id').values()
    tipoprestamo = TipoPrestamo.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/table_capital_prestamos.html')
    context = {
        'capitalprestamos': capitalprestamos,
        'tipoprestamo': tipoprestamo,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_capital_prestamos(request):

    tipoprestamo = TipoPrestamo.objects.all().order_by('id').values()
    #grupos = Group.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/form_capital_prestamos.html')
    context = {
        'tipoprestamo': tipoprestamo,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_capital_prestamos_store(request):

    if request.method == "POST":

        try:
            CapitalPrestamos.objects.create(
                id_user=1,
                id_etapas=1,
                tipo_prestamo=request.POST["tipo_prestamo"],
                fecha_prestamo=request.POST["fecha_prestamo"],
                tiempo_prestamo=request.POST["tiempo_prestamo"],
                taza_interes_prestamo=request.POST["taza_interes_prestamo"],
                monto_solicitado_prestamo=request.POST["monto_solicitado_prestamo"],
                firma_prestamo=request.POST["firma_prestamo"],
                status_prestamo=1
            )
            return redirect("/table_capital_prestamos")
        except:
            pass

    return redirect("/table_capital_prestamos")

    #grupos = Group.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/form_capital_inversion.html')
    context = {
        'alert': "",
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def table_tipo_prestamo(request):

    tipoprestamo = TipoPrestamo.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/table_tipo_prestamo.html')
    context = {
        'tipoinversion': tipoprestamo,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def form_tipo_prestamo(request):

    #tipoinversion = TipoInversion.objects.all().order_by('id').values()
    #usuario = User.objects.all().exclude(id=2).exclude(id=3)
    template = loader.get_template('home/form_tipo_prestamo.html')
    context = {
        #'tipoinversion': tipoinversion,
        'alert': "",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def form_tipo_prestamo_store(request):

    if request.method == "POST":

        verificando = TipoPrestamo.objects.filter(name_tipo_prestamo=request.POST["name_tipo_prestamo"]).exists()
        if verificando == False:
            try:
                TipoPrestamo.objects.create(
                    name_tipo_prestamo=request.POST["name_tipo_prestamo"],
                    calculo_prestamo=request.POST["calculo_prestamo"],
                    calculo_prestamo_valor=request.POST["calculo_prestamo_valor"]
                )
                return redirect("/table_tipo_prestamo")
            except:
                pass

    return redirect("/table_tipo_prestamo")


# CAPITAL DE PRESTAMOS

# GENERAL

def destroyCapital(request, id, modelo):
    if modelo == 1:
        dele = CapitalInversion.objects.get(id=id)
        dele.delete()
        return redirect("/table_capital_inversion")
    elif modelo == 2:
        dele = CapitalOperaciones.objects.get(id=id)
        dele.delete()
        return redirect("/table_capital_operaciones")
    elif modelo == 3:
        dele = CapitalPrestamos.objects.get(id=id)
        dele.delete()
        return redirect("/table_capital_prestamos")
    elif modelo == 4:
        dele = TipoInversion.objects.get(id=id)
        dele.delete()
        return redirect("/table_capital_prestamos")
    elif modelo == 5:
        dele = TipoPrestamo.objects.get(id=id)
        dele.delete()
        return redirect("/table_capital_prestamos")




#  ETAPAS DEL USUARIO

@login_required(login_url="/login/")
def etapa_id(request, id):

    etapa = Etapas.objects.filter(id_user=id)
    template = loader.get_template('home/index_etapa.html')
    context = {
        'etapa': etapa,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
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


'''@login_required(login_url="/login/")
def etapa(request):

    etapa = Etapas.objects.all()
    template = loader.get_template('home/index_etapa.html')
    context = {
        'etapa': etapa,
    }
    return HttpResponse(template.render(context, request))



@login_required(login_url="/login/")
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
    #return HttpResponse(template.render(context, request))'''




#  ETAPAS DEL USUARIO



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

