from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User, models, Votant, Idee
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
        
class Idea(ModelForm):
    class Meta:
        model=  Idee
        fields=['formulation','detail']