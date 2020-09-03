from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Publicar
from django.urls import reverse_lazy
from .forms import PublicarForm,ModificarPublicacionForm

# Create your views here.

#def blog(request):
 #   return render(request,'blog/publicar.html')

class PublicarListView(ListView):
    model = Publicar
    template_name = 'blog/publicar.html'
    ordering = ['-publication_date']

class PublicarDetailView(DetailView):
    model = Publicar
    template_name = 'blog/publicacion_detalle.html'

class PublicarCreateView(CreateView):
    model = Publicar
    form_class = PublicarForm
    template_name = 'blog/agregar_publicacion.html'
    #fields = '__all__'

class PublicarDeleteView(DeleteView):
    model = Publicar
    template_name = 'blog/eliminar_publicacion.html'
    success_url = reverse_lazy('publicar')

class ModificarPublicacionUpdateView(UpdateView):
    model = Publicar
    form_class = ModificarPublicacionForm
    template_name = 'blog/modificar_publicacion.html'
    success_url = reverse_lazy('publicar')

   