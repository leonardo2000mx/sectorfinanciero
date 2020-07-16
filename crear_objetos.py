import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sectorFinanciero.settings')
django.setup()

from empresas.models import Sector, Empresa,PrecioEmpresa

import mysql.connector,operaciones

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="prueba"
)

mycursor = mydb.cursor()

def sectores():
    mycursor.execute("SELECT nombreSector, sectorTicker FROM sectores")

    sectores = mycursor.fetchall()

    for sector in sectores:
        nombreSector = sector[0]
        tickerSector = sector[1] 
        sector = Sector.objects.get_or_create(nombre=nombreSector,ticker=tickerSector)

def empresa():
    mycursor.execute("SELECT nombre, pais, ticker, id_sector, sector, industria, descripcion FROM datosgenerales")

    empresas = mycursor.fetchall()

    for empresa in empresas:
        nombre = empresa[0]
        pais = empresa[1] 
        ticker = empresa[2]
        id_sector = empresa[3]
        sector = empresa[4]
        industria = empresa[5]
        descripcion = empresa[6]
        empresa = Empresa.objects.get_or_create(nombre=nombre,pais=pais, ticker=ticker,id_sector=Sector.objects.get(pk=id_sector),sector=sector,industria=industria,descripcion=descripcion)


def precioEmpresa(empresa):
    mycursor.execute("SELECT id_empresa, nombre_empresa, Fecha, Open, High, Low, Close, Volume FROM "+ empresa)

    empresas = mycursor.fetchall()

    for empresa in empresas:
        id_empresa = empresa[0]
        nombre_empresa = empresa[1] 
        Fecha = empresa[2]
        Open = empresa[3]
        High = empresa[4]
        Low = empresa[5]
        Close = empresa[6]
        Volume = empresa[7]
        empresa = PrecioEmpresa.objects.get_or_create(id_empresa=Empresa.objects.get(pk=id_empresa),
        nombre_empresa=nombre_empresa, fecha=Fecha,precio_apertura=Open,precio_maximo=High,
        precio_minimo=Low,precio_cierre=Close, volumen=Volume)

#sectores()
#empresa()

empresas=["AC","AEROMEX","AGUA","ALFAA","ALPEKA","ALSEA","AMXL","ARA","ASURB","AUTLANB","AXTELCPO",
"BACHOCOB","BBAJIOO","BIMBOA","BOLSAA","BSMXB","CADUA","CEMEXCPO","CHDRAUIB","CIDMEGA","CIEB",
"CREAL","CUERVO","ELEKTRA","ELEMENT","FEMSAUBD","FINDEP","FRAGUAB","GAPB",
"GCARSOA1","GCC","GFAMSAA","GFINBURO","GFNORTEO","GICSAB","GIGANTE","GMEXICOB","GMXT",
"HCITY","HERDEZ","HOTEL","ICHB","IENOVA","KIMBERA","KOFUBL","LABB","LACOMERUBC","LALAB","LAMOSA",
"LIVEPOLC","MEGACPO","MFRISCOA","NEMAKA","OMAB","PAPPEL","PENOLES","PINFRA","POSADASA","Q","RA",
"SIMECB","SITESB","SORIANAB","SPORTS","TLEVISACPO","TRAXIONA","UNIFINA","VESTA","VITROA","VOLARA","WALMEX"]

for empresa in empresas:
    precioEmpresa(empresa)

