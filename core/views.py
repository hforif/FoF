from django.shortcuts import render
from core.models import Profile, CustomAnimal
from django.contrib.auth.models import User


# Create your views here.
def show_animal_list(request):
    user = User.objects.get(username='asus')
    profile = Profile.objects.get(user=user)
    animals = CustomAnimal.objects.filter(owner=profile)
    return render(request, 'core/animal_list.html', {'animals': animals})


def add_animal(request):
    return render(request, 'core/animal_edit.html')
