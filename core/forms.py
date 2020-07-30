from django import forms
from .models import Profile, CustomAnimal


class FarmForm(forms.Form):
    owner = forms.ModelChoiceField(Profile.objects.all())
    name = forms.CharField(max_length=20)
    donkey = forms.BooleanField()
    dog = forms.BooleanField()
    cat = forms.BooleanField()
    rooster = forms.BooleanField()
    chick = forms.BooleanField()
    custom_animals = forms.ModelMultipleChoiceField(CustomAnimal.objects.all())
