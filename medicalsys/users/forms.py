from django import forms


class RegisterUserForms(forms.Form):
    name = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite a sua senha',
                'minlength': 6,
            }
        ),
    )
    password_confirm = forms.CharField(
        label='Confirme a sua senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite a sua senha novamente',
                'minlength': 6,
            }
        ),
    )


class LoginUserForms(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite a sua senha',
                'minlength': 6,
            }
        ),
    )
