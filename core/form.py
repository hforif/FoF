from django import forms
from .models import CustomAnimal


class CustomAnimalForm(forms.ModelForm):
    class Meta:
        model = CustomAnimal
        fields = ['owner', 'name', 'photo', 'audio']