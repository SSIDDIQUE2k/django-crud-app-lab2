# main_app/views.py
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Animal

class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'breed', 'description', 'age']

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['breed', 'description', 'age']

class AnimalDelete(DeleteView):
    model = Animal
    success_url = '/animals/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animal_index(request):
    animals = Animal.objects.all()
    return render(request, 'animals/index.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    feeding_form = FeedingForm()
    return render(request, 'animals/detail.html', {'animal': animal, 'animal': animal, 'feeding_form': feeding_form})

def add_feeding(request, animal_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.animal_id = animal_id
        new_feeding.save()
    return redirect('animal-detail', animal_id=animal_id)
