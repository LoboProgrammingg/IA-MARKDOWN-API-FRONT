# core/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

tailwind_input_classes = {
    'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm transition duration-150 ease-in-out focus:outline-none focus:ring-2 focus:ring-uggovBlue focus:border-transparent'
}

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs=tailwind_input_classes))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(attrs=tailwind_input_classes))
    first_name = forms.CharField(label='Primeiro Nome', required=False, widget=forms.TextInput(attrs=tailwind_input_classes))
    last_name = forms.CharField(label='Sobrenome', required=False, widget=forms.TextInput(attrs=tailwind_input_classes))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    unidade = forms.CharField(label='Unidade/Setor', required=False, widget=forms.TextInput(attrs=tailwind_input_classes))
    image = forms.ImageField(label='Foto de Perfil', required=False, widget=forms.FileInput)
    
    class Meta:
        model = Profile
        fields = ['unidade', 'image']