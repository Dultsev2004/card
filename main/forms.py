from os import path
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import views
from .models import Services, CustomUser, Order


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Введите логин')
    email = forms.EmailField(label='Введите Email')
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Введите логин', widget=forms.TextInput)
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)


class ServiceCreateForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput)
    description = forms.CharField(label='Описание', widget=forms.TextInput)
    image = forms.ImageField(label='Изображение')
    code = forms.CharField(label='Код')

    class Meta:
        model = Services
        fields = ('title', 'description', 'image', 'code')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"