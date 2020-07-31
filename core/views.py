from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile, Farm, CustomAnimal, Farmer
from .forms import FarmForm


def farm_list(request):
    qs = Farm.objects.all()

    return render(request, 'core/farm_list.html', {
        'farm_list': qs,
    })


def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    farmers = Farmer.objects.filter(farm=farm)
    return render(request, 'core/farm_detail.html', {'farm': farm, 'farmers': farmers})


def create_farm(request):
    profile = Profile.objects.get(pk=1)
    animals = CustomAnimal.objects.filter(owner=profile)

    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            farm = form.save()
            # farm = Farm.objects.create(**form.cleaned_data)
            for animal in animals:
                if request.POST.get(f'{animal.name}'):
                    Farmer.objects.create(farm=farm, custom_animal=animal, is_placed=True)
            return redirect('farm_list')
    else:
        form = FarmForm()

    return render(request, 'core/create_farm.html', {
        'form': form,
        'animals': animals,
    })


def edit_farm(request, pk):
    profile = Profile.objects.get(pk=1)
    animals = CustomAnimal.objects.filter(owner=profile)
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES, instance=farm)
        if form.is_valid():
            farm = form.save()
            for animal in animals:
                if request.POST.get(f'{animal.name}'):
                    Farmer.objects.create(farm=farm, custom_animal=animal, is_placed=True)
                    print(animal.name, '생성함')
            return redirect('farm_detail', pk=farm.pk)
    else:
        form = FarmForm(instance=farm)
    return render(request, 'core/create_farm.html', {
        'form': form,
        'animals':animals,
    })


def show_animal_list(request):
    user = User.objects.get(username='dayoung')
    profile = Profile.objects.get(user=user)
    animals = CustomAnimal.objects.filter(owner=profile)
    return render(request, 'core/animal_list.html', {'animals': animals})


def add_animal(request):
    return render(request, 'core/animal_edit.html')
