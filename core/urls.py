# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

"""

RUTAS PRINCIPALE DEL SISTEMA, LAS RUTAS QUE ESTAN EN apps/home/urls TAMBIEN DEBEN ESTAR AQUI

"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    path("usuarios/", include("apps.home.urls")),
    path("create_user/", include("apps.home.urls")),
    path("store_user/", include("apps.home.urls")),
    path("add_info_adicional_user/<int:id>", include("apps.home.urls")),
    path("add_info_adicional_store_user/<int:id>", include("apps.home.urls")),


    # capital de inversion
    path("table_capital_inversion/", include("apps.home.urls")),
    path("form_capital_inversion/", include("apps.home.urls")),
    path("form_capital_inversion_store/", include("apps.home.urls")),
    path("form_capital_inversion_edit/<int:id>", include("apps.home.urls")),

    path("table_tipo_inversion/", include("apps.home.urls")),
    path("form_tipo_inversion/", include("apps.home.urls")),
    path("form_tipo_inversion_store/", include("apps.home.urls")),

    # capital de operaciones
    path("table_capital_operaciones/", include("apps.home.urls")),
    path("form_capital_operaciones/", include("apps.home.urls")),
    path("form_capital_operaciones_store/", include("apps.home.urls")),

    # capital de prestamos
    path("table_capital_prestamos/", include("apps.home.urls")),
    path("form_capital_prestamos/", include("apps.home.urls")),
    path("form_capital_prestamos_store/", include("apps.home.urls")),


    path("table_tipo_prestamo/", include("apps.home.urls")),
    path("form_tipo_prestamo/", include("apps.home.urls")),
    path("form_tipo_prestamo_store/", include("apps.home.urls")),

    # General

    path("destroyCapital/<int:id>/<int:modelo>", include("apps.home.urls")),



    path("etapa/", include("apps.home.urls")),
    path("etapa_id/<int:id>", include("apps.home.urls")),
    #path("edit_status_etapa_id/<int:id>/<int:idu>", include("apps.home.urls")),
    path("edit_status_etapa/<int:id>", include("apps.home.urls"))
]
