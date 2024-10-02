from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Post
from messaging.models import Message


# Formulario para registro de usuario
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Formulario para editar perfil
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']


# Formulario para crear y editar posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'body', 'image']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']