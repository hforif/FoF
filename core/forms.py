from django import forms
from .models import Farm, CustomAnimal, Farmer


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['owner', 'name', 'donkey', 'dog', 'cat', 'rooster', 'chick']

