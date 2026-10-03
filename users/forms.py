from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'email', 'phone','is_boss']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'phone','is_boss']