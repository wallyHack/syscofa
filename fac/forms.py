
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""
        model = Cliente
        fields = ['nombres', 'apellidos', 'tipo', 'celular', 'estado']
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #iteramos todos los campos del form
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    

