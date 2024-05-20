from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django import forms

#on peut personnaliser cette classe, l'étendre

class UserCreationFormCustom (UserCreationForm):   #nouvelle classe (qui hérite de usercreationform)
    class Meta (UserCreationForm.Meta):
        model=User
        # fields= ['username','email','password1','password2','role']
        fields= '__all__'
        
        
class RegisterForm(UserCreationForm):
    # birthdate = forms.DateField()
    
    # email= forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "birth_date", "email","role","first_name", "last_name"]
        
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


class LoginForm(UserCreationForm):
    # birthdate = forms.DateField()
    
    # email= forms.EmailField()
    class Meta:
        model = User
        fields = ["email","password1"]
        
# class RegisterForm(UserCreationForm):
#     birthdate = forms.DateField()
    
#     email= forms.EmailField()
#     class Meta:
#         model = User
#         fields = ["username", "password1", "password2", "birthdate", "email"]
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')