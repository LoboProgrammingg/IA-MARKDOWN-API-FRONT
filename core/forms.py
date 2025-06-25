# core/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

tailwind_input_classes = {
    'class': 'w-full px-4 py-2 border border-slate-300 dark:border-slate-600 rounded-lg shadow-sm bg-slate-50 dark:bg-slate-700 text-slate-800 dark:text-slate-200 placeholder-slate-400 dark:placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-uggovBlue focus:border-transparent transition duration-150 ease-in-out'
}


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput(attrs=tailwind_input_classes),
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(attrs=tailwind_input_classes),
    )
    first_name = forms.CharField(
        label='Primeiro Nome',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seu primeiro nome',
                **tailwind_input_classes,
            }
        ),
    )
    last_name = forms.CharField(
        label='Sobrenome',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Seu sobrenome', **tailwind_input_classes}
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['unidade', 'image']
        labels = {'unidade': 'Unidade/Setor', 'image': 'Foto de Perfil'}
        widgets = {
            'unidade': forms.Select(
                attrs={
                    'class': 'w-full px-4 py-2 border border-slate-300 dark:border-slate-600 rounded-lg shadow-sm bg-slate-50 dark:bg-slate-700 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-uggovBlue focus:border-transparent transition duration-150 ease-in-out'
                }
            ),
            'image': forms.FileInput(attrs={'class': 'hidden'}),
        }
