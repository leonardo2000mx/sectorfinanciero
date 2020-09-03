from django.shortcuts import render,HttpResponse, get_object_or_404,redirect
from .models import Sector,PrecioEmpresa,Empresa, PrecioSector
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import SectorSerializer, EmpresaSerializer, PrecioempresaSerializer, PreciosectorSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.

@login_required(login_url='acceso/')
def index(request):
    Sectores = Sector.objects.all()
    context = {'Sectores': Sectores }
    return render (request,"empresas/index.html",context)

@login_required(login_url='acceso/')
def sectores(request):
    Sectores = Sector.objects.all()
    context = {'Sectores': Sectores }
    return render (request,"empresas/sectores.html",context)

@login_required(login_url='acceso/')
def sector(request,id):
    sector = get_object_or_404(Sector, pk=id)
    return render (request,"empresas/sector.html",{"sector":sector})

@login_required(login_url='acceso/')
def precio_empresas(request,id):
    precio_empresa = get_object_or_404(PrecioEmpresa, pk=id)
    return render (request,"empresas/precio_empresas.html",{"precio_empresa":precio_empresa})

@login_required(login_url='acceso/')
def empresas(request):
    queryset = request.GET.get("buscar")
    empresas = Empresa.objects.all()
    if queryset:
        empresas = Empresa.objects.filter(
            nombre__icontains=queryset
        )
    paginator = Paginator(empresas, 10)
    page = request.GET.get('page')


    try:
        empresas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        empresas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        empresas= paginator.page(paginator.num_pages)


    # precios_empresa = empresa.precioempresa_set.all()
    return render(request,"empresas/empresas.html",{"empresas":empresas})


@login_required(login_url='acceso/')
def empresa(request,id):
    empresa = Empresa.objects.get(pk=id)
    precios_empresa = empresa.emp.all()
    return render(request,"empresas/empresa.html",{"precios_empresa":precios_empresa,"empresa":empresa})

def registro(request):
    if request.user.is_authenticated:
        return redirect('index/')
    
    else: 
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'La cuenta se ha registrado' + user)

                return redirect('registro')

        context = {
            'form':form
        }
        return render(request,'empresas/registro.html',context)

def acceso(request):

    if request.user.is_authenticated:
        return redirect('/')

    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('/') 

            else:
                messages.info(request,'Username OR password is incorrect')
                
        return render(request,'empresas/acceso.html')

def salidaUsuario(request):
    logout(request)
    return render(request,'empresas/acceso.html')


class LineChartJSONView(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        #return ("January", "February", "March", "April", "May", "June", "July")
        empresa = Empresa.objects.get(pk=3)
        precios_empresa = empresa.emp.all()

        fechas = []
        for precio_empresa in precios_empresa:
            fechas.append(precio_empresa.fecha)

        return fechas


    def get_providers(self):
        """Return names of datasets."""
        return ["Central"]

    def get_data(self):

        empresa = Empresa.objects.get(pk=3)
        precios_empresa = empresa.emp.all()

        precioCierre = []
        for precio_empresa in precios_empresa:
            precioCierre.append(precio_empresa.precio_cierre)


        return [precioCierre]

        #return [[75, 44, 92, 11, 44, 95, 35],
         #       [41, 92, 18, 3, 73, 87, 92],
          #      [87, 21, 94, 3, 90, 13, 65]]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

def line_chart_json2(request,id):
    labels = []
    data = []

    #queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')

    empresa = Empresa.objects.get(pk=id)
    precios_empresa = empresa.emp.all()

    for precio_empresa in precios_empresa:
        labels.append(precio_empresa.fecha)
        data.append(precio_empresa.precio_cierre)

    return JsonResponse(data={
        'labels': labels,
        'datasets': [{'data':data,
        "backgroundColor": "rgba(202, 201, 197, 0.5)",
        "borderColor": "rgba(202, 201, 197, 1)",
        "pointBackgroundColor": "rgba(202, 201, 197, 1)",
        "pointBorderColor": "#fff",
        "label": "Central",
        "name": "Central"}],
    })



class SectorViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla sector
    """
    # Se define el conjunto de datos sobre el que va a operar la vita,
    # en este caso, sobre todos los usuarios disponibles.
    queryset = Sector.objects.all().order_by('id')

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = SectorSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla sector
    """
    # Se define el conjunto de datos sobre el que va a operar la vita,
    # en este caso, sobre todos los usuarios disponibles.
    queryset = Empresa.objects.all().order_by('id')

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = EmpresaSerializer

class PrecioempresaViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla sector
    """
    # Se define el conjunto de datos sobre el que va a operar la vita,
    # en este caso, sobre todos los usuarios disponibles.
    queryset = PrecioEmpresa.objects.all()

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = PrecioempresaSerializer

class PreciosectorViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones con la tabla sector
    """
    # Se define el conjunto de datos sobre el que va a operar la vita,
    # en este caso, sobre todos los usuarios disponibles.
    queryset = PrecioSector.objects.all()

    # Se define el serializador encargado de transformar las peticiones
    # de json a objetos django y viceversa.
    serializer_class = PreciosectorSerializer


