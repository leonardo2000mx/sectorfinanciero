from rest_framework import serializers

from .models import Sector, Empresa, PrecioEmpresa,PrecioSector 


class SectorSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """
    class Meta:
        # Se define sobre que modelo actúa
        model =Sector
        # Se definen los campos a incluir
        fields = ('nombre','ticker')



class PrecioempresaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    class Meta:
        # Se define sobre que modelo actúa
        model = PrecioEmpresa
        # Se definen los campos a incluir
        fields = ( 'nombre_empresa', 'fecha', 'precio_apertura', 'precio_maximo',
            'precio_minimo', 'precio_cierre','volumen')


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tour """
    emp= PrecioempresaSerializer(many=True)
    
    class Meta:
        # Se define sobre que modelo actúa
        model = Empresa
        # Se definen los campos a incluir
        fields = ('nombre', 'pais', 'ticker','id_sector','sector','industria','descripcion','emp')



class PreciosectorSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    class Meta:
        # Se define sobre que modelo actúa
        model = PrecioSector
        # Se definen los campos a incluir
        fields = ('id_sector', 'nombre_sector', 'fecha', 'precio_apertura', 'precio_maximo',
            'precio_minimo', 'precio_cierre','volumen')