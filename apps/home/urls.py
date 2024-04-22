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
    path('create_user', views.create_user, name='create_user'),
    path('store_user', views.store_user, name='store_user'),
    path('add_info_adicional_user/<int:id>', views.add_info_adicional_user, name='add_info_adicional_user'),
    path('add_info_adicional_store_user/<int:id>', views.add_info_adicional_store_user, name='add_info_adicional_store_user'),

    # capital de inversion
    path('table_capital_inversion', views.table_capital_inversion, name='table_capital_inversion'),
    path('form_capital_inversion', views.form_capital_inversion, name='form_capital_inversion'),
    path('form_capital_inversion_store', views.form_capital_inversion_store, name='form_capital_inversion_store'),
    path('form_capital_inversion_edit/<int:id>', views.form_capital_inversion_edit, name='form_capital_inversion_edit'),

    path('table_tipo_inversion', views.table_tipo_inversion, name='table_tipo_inversion'),
    path('form_tipo_inversion', views.form_tipo_inversion, name='form_tipo_inversion'),
    path('form_tipo_inversion_store', views.form_tipo_inversion_store, name='form_tipo_inversion_store'),

    # capital de operaciones
    path('table_capital_operaciones', views.table_capital_operaciones, name='table_capital_operaciones'),
    path('form_capital_operaciones', views.form_capital_operaciones, name='form_capital_operaciones'),
    path('form_capital_operaciones_store', views.form_capital_operaciones_store, name='form_capital_operaciones_store'),


    # capital de prestamos
    path('table_capital_prestamos', views.table_capital_prestamos, name='table_capital_prestamos'),
    path('form_capital_prestamos', views.form_capital_prestamos, name='form_capital_prestamos'),
    path('form_capital_prestamos_store', views.form_capital_prestamos_store, name='form_capital_prestamos_store'),

    # calculo cuotas de prestamos
    path('form_calculo_cuota_prestamo', views.form_calculo_cuota_prestamo, name='form_calculo_cuota_prestamo'),

    path('table_tipo_prestamo', views.table_tipo_prestamo, name='table_tipo_prestamo'),
    path('form_tipo_prestamo', views.form_tipo_prestamo, name='form_tipo_prestamo'),
    path('form_tipo_prestamo_store', views.form_tipo_prestamo_store, name='form_tipo_prestamo_store'),

    # general
    path('destroyCapital/<int:id>/<int:modelo>', views.destroyCapital, name='destroyCapital'),


    path('etapa_id/<int:id>', views.etapa_id, name='etapa_id'),
    path('edit_status_etapa/<int:id>', views.edit_status_etapa, name='edit_status_etapa'),
    #path('etapa', views.etapa, name='etapa'),
    #path('edit_status_etapa_id/<int:id>/<int:idu>', views.edit_status_etapa_id, name='edit_status_etapa_id'),


    path('perfil/<int:id>', views.perfil, name='perfil'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
