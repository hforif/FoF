from django.shortcuts import render, redirect
from core.models import Profile, CustomAnimal
from django.contrib.auth.models import User
from core.form import CustomAnimalForm


# Create your views here.
def show_animal_list(request):
    user = User.objects.get(username='asus')
    profile = Profile.objects.get(user=user)
    animals = CustomAnimal.objects.filter(owner=profile)
    return render(request, 'core/animal_list.html', {'animals': animals})


def add_animal(request):
    if request.method == 'POST':
        form = CustomAnimalForm(request.POST, request.FILES)    # animal.photo = request.FILES.get('photo', False)
                                                                # animal.audio = request.FILES.get('audio', False)
        if form.is_valid():
            animal = form.save(commit=False)
            # animal.owner = request.user의 프로필
            animal.save()

        return redirect('show_animal_list')
    else:
        form = CustomAnimalForm()
    return render(request, 'core/animal_edit.html', {'form': form})
