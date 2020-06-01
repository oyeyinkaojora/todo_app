from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'