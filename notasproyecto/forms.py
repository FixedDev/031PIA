from django import forms

from notasproyecto.models import Nota


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido']
