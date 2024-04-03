# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

"""

ESTAS SON LAS RUTAS A LAS DIFERENTES PAGINAS Y ACTUALIZACION DE LOS ESTADO DEL USUARIO

"""


from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('usuarios', views.usuarios, name='usuarios'),
    path('etapa', views.etapa, name='etapa'),
    path('etapa_id/<int:id>', views.etapa_id, name='etapa_id'),
    path('edit_status_etapa_id/<int:id>/<int:idu>', views.edit_status_etapa_id, name='edit_status_etapa_id'),
    path('edit_status_etapa/<int:id>', views.edit_status_etapa, name='edit_status_etapa'),

    path('perfil/<int:id>', views.perfil, name='perfil'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
