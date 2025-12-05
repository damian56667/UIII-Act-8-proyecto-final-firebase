# backend_supermercado/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supermercado/', include('app_supermercado.urls')),
    path('', lambda request: redirect('supermercado/')),  # redirige la raíz a /supermercado/
]
