from django.shortcuts import render
from .models import PokemonCard, Trainer

def pokemon(request):
    # Use your models as needed
    cards = PokemonCard.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'pokemon.html',{'cards': cards, 'trainers': trainers})

def trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer.html', {'trainers': trainers})
