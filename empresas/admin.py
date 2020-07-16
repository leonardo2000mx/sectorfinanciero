from django.contrib import admin
from .models import Sector,Empresa,PrecioEmpresa,PrecioSector

# Register your models here.
admin.site.register(Sector)
admin.site.register(Empresa)
admin.site.register(PrecioEmpresa)
admin.site.register(PrecioSector)
