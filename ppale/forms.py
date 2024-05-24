from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User, models, Votant, Idee,  UserSelection
from django import forms
from django.forms import ModelForm


# class Voter(ModelForm):
   
#     class Meta:
#         model = Votant
#         fields = ['type_vote']
        

class Voter(ModelForm):
   
    class Meta:
        model = Votant
        fields = '__all__'


class aliments(ModelForm):
   
    class Meta:
        model = UserSelection
        fields = '__all__'
        widgets = {
            'legume': forms.Select(choices=UserSelection.legume_choices),
            'viande': forms.Select(choices=UserSelection.viande_choices),
            'feculent': forms.Select(choices=UserSelection.feculent_choices),
            'poisson':forms.Select(choices=UserSelection.poisson_choices),
            'type_repas':forms.Select(choices=UserSelection.repas_choices),
            'temps_préparation_souhaité':forms.Select(choices=UserSelection.temps_choices)
            # Ajoutez d'autres widgets ici pour les autres catégories
        }
class Idea(ModelForm):
    class Meta:
        model=  Idee
        fields=['formulation','detail']

class Idea(ModelForm):
    class Meta:
        model=  Idee
        fields=['formulation','detail']


class Idea(ModelForm):
    class Meta:
        model=  Idee
        fields=['formulation','detail']