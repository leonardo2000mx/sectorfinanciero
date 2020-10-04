from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Publicar,Category
from django.urls import reverse_lazy
from .forms import PublicarForm,ModificarPublicacionForm


# Create your views here.

#def blog(request):
 #   return render(request,'blog/publicar.html')

class PublicarListView(ListView):
    model = Publicar
    template_name = 'blog/publicar.html'
    ordering = ['-publication_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PublicarListView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'blog/category_list.html',{'category_menu_list':cat_menu_list})

class PublicarDetailView(DetailView):
    model = Publicar
    template_name = 'blog/publicacion_detalle.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PublicarDetailView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

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

def CategoryView(request,cats):
    category_posts = Publicar.objects.filter(category=cats.replace('-',' '))
    return render(request,'blog/categorias.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'blog/agregar_categoria.html'
    fields = '__all__'

