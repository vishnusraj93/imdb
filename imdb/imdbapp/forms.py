import imp
from socket import fromshare
from django import forms
from . models import Movie

class Movie_Form(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'image']