from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['author','name','brand','description','price','size','type','gender','image']

# Form that allows the user to create an account
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    # Stores the user attributes for each user
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']