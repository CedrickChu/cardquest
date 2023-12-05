from django.shortcuts import render
from .models import PokemonCard, Trainer, Collection

def pokemon(request):
    cards = PokemonCard.objects.all()
    return render(request, 'pokemon.html',{'cards': cards})

def trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer.html', {'trainers': trainers})

def collection(request):
    collections = Collection.objects.all()
    return render(request, 'collection.html', {'collections': collections})

