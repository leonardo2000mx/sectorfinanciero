"""sectorFinanciero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('precio_empresas/<int:id>', views.precio_empresas, name='precio_empresas'),
    path('sectores', views.sectores, name='sectores'),   
    path('sector/<int:id>', views.sector, name='sector'),
    path('empresas', views.empresas, name='empresas'),
    path('empresa/<int:id>', views.empresa, name='empresa'),
    path('chart/<int:id>', views.line_chart, name='line_chart'),
    path('chart3/<int:id>', views.line_chart, name='line_chart3'),
    path('chartJSON/<int:id>', views.line_chart_json2, name='line_chart_json'),
    path('chartJSON3/<int:id>', views.line_chart_json3, name='line_chart_json3'),
    path('registro/', views.registro, name='registro'),
    path('acceso/', views.acceso, name='acceso'),
    path('salida/', views.salidaUsuario, name='salida'),
    path('', views.index, name='index'),
]
