
from django import forms
from .models import clientes,campaña, paquete

class ClientesForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = ('nombre_cliente', 'razon_social','nombre_contacto','puesto','telefono_contacto','email_contacto','email_empresa'
        ,'telefono_empresa','direccion_empresa','cfdi')
        widgets={
            
            'nombre_cliente': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre de la empresa',
                    'id':'nombre_cliente',
                    'required': 'required',
                }
            ),
            'razon_social': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Razon social de empresa',
                    'id':'razon_social',
                    'required': 'required',
                }
            ),
            'nombre_contacto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Nombre del contacto',
                    'id':'nombre_contacto',
                    'required': 'required',
                }
            ),
            'puesto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Puesto del contacto',
                    'id':'puesto',
                    'required': 'required',
                }
            ),
            'telefono_contacto': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Telefono del contacto',
                    'id':'telefono_contacto',
                    'required': 'required',
                }
            ),
            'email_contacto': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Introducir el email del contacto',
                    'id':'email_contacto',
                    'required': 'required',
                }
            ),
            'email_empresa': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Email de la empresa',
                    'id':'email_empresa',
                    'required': 'required',
                }
            ),
            'telefono_empresa': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Telefono de la empresa',
                    'id':'telefono_empresa',
                    'required': 'required',
                }
            ),
            'direccion_empresa': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Dirección de la empresa',
                    'id':'direccion_empresa',
                    'required': 'required',
                }
            ),
            'cfdi': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Uso de CFDI',
                    'id':'cfdi',
                    'required': 'required',
                }
            ),
        }

class CampañasForm(forms.ModelForm):
    class Meta:
        model = campaña
        fields = ('nombre_campaña', 'status','categoria','video','imagen','cliente','paquete','fecha_inicial','fecha_final')
        widgets={
            
            'nombre_campaña': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre de la campaña',
                    'id':'nombre_campaña',
                    'required': 'required',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class':'form-select',
                    'placeholder': 'Estado de la campaña',
                    'id':'status',
                    'required': 'required',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class':'form-select',
                    'placeholder': 'Categoria',
                    'id':'categoria',
                    'required': 'required',
                }
            ),
            'paquete': forms.Select(
                attrs={
                    'class':'form-select',
                    'placeholder': 'Tipo de paquete ',
                    'id':'paquete',
                    'required': 'required',
                }
            ),  
            'cliente': forms.Select(
                attrs={
                    'class':'form-select',
                    'placeholder': 'Cliente',
                    'id':'cliente',
                    'required': 'required',
                }
            ),
            'video': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'type':'file',
                    'id':'video',
                    'required': 'required',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'type':'file',
                    'id':'imagen',
                    'required': 'required',
                }
            ),
            'fecha_inicial': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date',
                    'id':'fecha_inicial',
                    'required': 'required',
                }
            ),
            'fecha_final': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date',
                    'id':'fecha_final',
                    'required': 'required',
                }
            ),      
           
        }
class PaquetesForm(forms.ModelForm):
    class Meta:
        model = paquete
        fields = ('nombre_paquete','duracion','frecuencia','precio')
        widgets={
            'nombre_paquete': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre del paquete',
                    'id':'nombre_paquete',
                    'required': 'required',
                }
            ),
            'duracion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Duración del paquete',
                    'id':'duracion',
                    'required': 'required',
                }
            ),
            'frecuencia': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Frecuencia del paquete',
                    'id':'paquete',
                    'required': 'required',
                }
            ),  
            'precio': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Precio',
                    'id':'precio',
                    'required': 'required',
                }
            ),           
        }