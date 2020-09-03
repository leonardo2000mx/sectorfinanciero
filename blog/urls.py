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

from django.urls import path, include
from .views import PublicarListView,PublicarDetailView,PublicarCreateView,PublicarDeleteView,ModificarPublicacionUpdateView


urlpatterns = [
    path('publicar/', PublicarListView.as_view(), name='publicar'),
    path('publicacion_detalle/<int:pk>', PublicarDetailView.as_view(), name='publicacion_detalle'),
    path('agregar_publicacion', PublicarCreateView.as_view(), name='agregar_publicacion'),
    path('modificar_publicacion/<int:pk>', ModificarPublicacionUpdateView.as_view(), name='modificar_publicacion'),
    path('publicacion_detalle/<int:pk>/eliminar', PublicarDeleteView.as_view(), name='eliminar_publicacion'),
]
