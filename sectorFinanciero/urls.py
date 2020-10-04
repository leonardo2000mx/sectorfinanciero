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
from django.urls import path, include
from rest_framework import routers
from empresas import views

router = routers.DefaultRouter()
router.register(r'sector', views.SectorViewSet)
router.register(r'empresa', views.EmpresaViewSet)
router.register(r'precioempresa', views.PrecioempresaViewSet)
router.register(r'preciosector', views.PreciosectorViewSet)

urlpatterns = [
    path('', include(('empresas.urls','empresas'), namespace='empresas')),
    path('blog/', include('blog.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),
    path('admin/', admin.site.urls),
        # Rutas para la url /api/
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls',
        namespace="rest_framework")),

]
