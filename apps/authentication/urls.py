# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.home import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('etapa_id/<int:id>', views.etapa_id, name='etapa_id'),
    path('edit_status_etapa_id/<int:id>/<int:idu>', views.etapa_id, name='etapa_id'),
]
