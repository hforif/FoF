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
    return render(request, 'core/farm_detail.html', {'farm':farm, 'farmers':farmers})


def create_farm(request):
    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farm_list')
    else:
        form = FarmForm()

    return render(request, 'core/create_farm.html', {
        'form': form,
    })


def edit_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES,instance=farm)
        if form.is_valid():
            farm = form.save()
            return redirect('farm_detail', pk=farm.pk)
    else:
        form = FarmForm(instance=farm)
    return render(request, 'core/create_farm.html', {
        'form':form,
    })


def show_animal_list(request):
    user = User.objects.get(username='dayoung')
    profile = Profile.objects.get(user=user)
    animals = CustomAnimal.objects.filter(owner=profile)
    return render(request, 'core/animal_list.html', {'animals': animals})


def add_animal(request):
    return render(request, 'core/animal_edit.html')
