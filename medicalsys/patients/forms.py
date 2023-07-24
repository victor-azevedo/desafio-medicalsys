from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'minlength': 14}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'minlength': 9}),
        }
        labels = {
            'name': 'Nome',
            'phone': 'Telefone',
            'address': 'Endereço',
            'address_number': 'Número',
            'city': 'Cidade',
            'uf': 'UF',
            'country': 'País',
            'cep': 'CEP'
        }
