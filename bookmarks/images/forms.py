from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class meta:
        model = Image
        fields = ['title','url','description']
        widgets = {
            'url' : forms.HiddenInput,
        }