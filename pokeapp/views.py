from django.shortcuts import render
from .models import PokemonCard, Trainer

def pokemon(request):
    cards = PokemonCard.objects.all()
    return render(request, 'pokemon.html',{'cards': cards})

def trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer.html', {'trainers': trainers})