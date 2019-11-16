from django import forms
from .models import Post

class reservform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('nombre', 'cemail', 'celular', 'fecha_reserva','text',)