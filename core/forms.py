from django import forms
from .models import Farm, Profile

class FarmForm(forms.Form):
    name = forms.CharField(max_length=20)
    donkey = forms.BooleanField()
    dog = forms.BooleanField()
    cat = forms.BooleanField()
    rooster = forms.BooleanField()
    chick = forms.BooleanField()

