from django import forms
from .models import Publicar

class PublicarForm(forms.ModelForm):
	class Meta:
		model = Publicar
		fields =('titulo', 'autor','cuerpo')
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}), 
			'autor': forms.TextInput(attrs={'class':'form-control'}),
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

