from django.db import models

# Create your models here.

class Sector(models.Model):
    nombre = models.CharField(max_length=50)
    ticker = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}, {self.ticker}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=20)
    ticker = models.CharField(max_length=20, null= True, blank=True)
    id_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    sector = models.CharField(max_length=50, null=True)
    industria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.nombre}, {self.ticker}"

class PrecioEmpresa(models.Model):
    id_empresa = models.ForeignKey(Empresa,on_delete= models.CASCADE)
    nombre_empresa = models.CharField(max_length=50)
    fecha = models.DateField()
    precio_apertura = models.FloatField()
    precio_maximo = models.FloatField()
    precio_minimo = models.FloatField()
    precio_cierre = models.FloatField()
    volumen = models.FloatField()

    def __str__(self):
        return f"{self.pk},{self.id_empresa}, {self.nombre_empresa}"

class PrecioSector(models.Model):
    id_sector = models.ForeignKey(Sector,on_delete= models.CASCADE)
    nombre_sector = models.CharField(max_length=50)
    fecha = models.DateField()
    precio_apertura = models.FloatField()
    precio_maximo = models.FloatField()
    precio_minimo = models.FloatField()
    precio_cierre = models.FloatField()
    volumen = models.FloatField()
    
    
