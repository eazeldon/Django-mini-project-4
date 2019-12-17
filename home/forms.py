from django import forms
from .models import home


class Djangoproject4Forms(forms.ModelForm):

    class Meta:
        model = home
        fields = ('image',)