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
    animals = CustomAnimal.objects.filter(owner=farm.owner)
    return render(request, 'core/farm_detail.html', {'farm':farm, 'animals':animals})


def create_farm(request, farm=None):
    # POST 요청 -> POST 데이터를 처리하는 역할
    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            farm = Farm.object.create(**form.cleaned_data)
            return redirect('/')
    # GET요청
    else:
        form = FarmForm()

    return render(request, 'core/create_farm.html', {
        'form': form,
    })


def edit_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return create_farm(request, farm)


# Create your views here.
def show_animal_list(request):
    user = User.objects.get(username='dayoung')
    profile = Profile.objects.get(user=user)
    animals = CustomAnimal.objects.filter(owner=profile)
    return render(request, 'core/animal_list.html', {'animals': animals})


def add_animal(request):
    return render(request, 'core/animal_edit.html')
