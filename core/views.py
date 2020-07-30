from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Farm, CustomAnimal
from .forms import FarmForm


def farm_list(request):
    qs = Farm.objects.all()

    return render(request, 'core/farm_list.html', {
        'farm_list':qs,
    })


def farm_detail(request):
    #farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'core/farm_detail.html')


def create_farm(request, farm=None):
    # POST 요청
    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            farm = form.save()
            return redirect('??')
    # GET요청
    else:
        form = FarmForm()
        return render(request, 'core/create_farm.html', {
            'form':form,
        })


def edit_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return create_farm(request, farm)