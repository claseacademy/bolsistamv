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
    path("etapa/", include("apps.home.urls")),
    path("etapa_id/<int:id>", include("apps.home.urls")),
    path("edit_status_etapa_id/<int:id>/<int:idu>", include("apps.home.urls")),
    path("edit_status_etapa/<int:id>", include("apps.home.urls"))
]
