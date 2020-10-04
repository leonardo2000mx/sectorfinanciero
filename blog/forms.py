from django import forms
from .models import Publicar,Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PublicarForm(forms.ModelForm):
	class Meta:
		model = Publicar
		fields =('titulo', 'autor','category','cuerpo')
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'autor' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}), 
			#'autor': forms.TextInput(attrs={'class':'form-control'}),
			'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
			'cuerpo':forms.Textarea(attrs={'class':'form-control'})
		}

class ModificarPublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicar
		fields =('titulo', 'cuerpo')
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}), 
			#'autor': forms.TextInput(attrs={'class':'form-control'}),
			'cuerpo':forms.Textarea(attrs={'class':'form-control'})
		}

