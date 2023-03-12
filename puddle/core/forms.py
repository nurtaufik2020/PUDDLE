from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

#tambahkan baris kode ini setelah Mengimport AuthenticationForm
class LoginForm(AuthenticationForm):
    attrs={
        'placeholder': 'Fill out this field',
        'class': 'w-full py-4 px-6 rounded-xl'
    }
    username = forms.CharField(widget=forms.TextInput(attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs))
    

class SignupForm(UserCreationForm):
    #class meta digunakan untuk menghubungkan form dengan models yang telah dibuat
    class Meta :
        model = User
        fields=('username','email','password1','password2')


    attrs={
        'placeholder': 'Fill out this field',
        'class': 'w-full py-4 px-6 rounded-xl'
    }
    username = forms.CharField(widget=forms.TextInput(attrs))
    email = forms.CharField(widget=forms.EmailInput(attrs))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs))
