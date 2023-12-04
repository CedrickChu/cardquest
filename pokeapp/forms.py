from django import forms
from .models import PokemonCard
from .models import Trainer

class PokemonCardForm(forms.ModelForm):
    class Meta:
        model = PokemonCard
        fields = '__all__' 
        
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__' 