#nombre
#apellidos
#foto
#cargo =>{1chef ; 2Admin ; 3Mesero ; 4Ayudante }
#salario
#contacto
from django import forms

class FormularioEmpleados(forms.Form):
    
    CARGO=(
        (1, 'Chef'),
        (2, 'Administrador'),
        (3, 'Mesero'),
        (4, 'Ayudante')
    )

    nombre=forms.CharField(
        required=True,
        max_length=50,
        label= 'Nombre del Empleado ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    apellidos=forms.CharField(
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(        
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=CARGO
    )
    salario=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    contacto=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    
    
    