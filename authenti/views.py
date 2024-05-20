from django.shortcuts import render
from django.views.generic import ListView, CreateView
from.forms import UserCreationForm, RegisterForm, LoginForm
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy

# Create your views here.
def home (request):
    
   
    return render (request, 'authenti/home.html')

# class Signup(CreateView):
#     form_class= UserCreationForm
#     template_name='authenti/signup.html'
@login_required
def homes (request):
    
   
    return render (request, 'authenti/homes.html')


class SignupPage(CreateView):
     success_url=reverse_lazy('login')
     template_name='authenti/signup.html'
     form_class= forms.RegisterForm


class LoginPageView(View):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = 'voici le formulaire à remplir, prenez votre temps'
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants malheuresementinvalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})
    
    
def logina(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(   #prend 2 arguments: nom utilisateur et mot de passe!
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)      # va servire pour se connecter, prend comme arguments: objets "request" et "user"
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authenti/login.html', context={'form': form, 'message': message})
    
    

    
def logout_user(request):
    
    logout(request)
    return redirect('login')    
     

@login_required
def home(request):
    return render(request, 'authenti/home.html')

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('home')
    return render(request, 'registration/signup.html', context={'form': form})


# def signup(request):
#     if request.method== "POST":
#         form= UserCreationform(request, data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request, user)
#             return redirect('profil_perso')
#     else:
#         form= UserCreationform(request)
        
    
#     return render (request, "authenti/signup.html", {'form':form})

def add_votant(request, nom_user_rdv):                                                    #donne la possibilité d'ajouter une note, fonctionalité disponible à partir de la liste de tous les rendez_vous
   
    user=nom_user_rdv
    if request.method == 'POST':
        form = Formu_note(request.POST)
        if form.is_valid():
            form.cleaned_data['client'] = user                                         #la note est assignée au client pour lequel le coach veut ajouter une note
            form.save()
            return redirect('list_all_rdv')
    else:
        form = Formu_note()
    return render(request, 'rendez_vous/add_note.html', {'form': form, 'client':user})
