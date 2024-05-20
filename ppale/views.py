from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from.models import Idee, Votant
from . import forms
from .forms import Voter, Idea
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import F

# Create your views here.
def home (request):
    
    return render (request, 'ppale/home.html')


def about (request):
    
    return render (request, 'ppale/about.html')



class IdeasListView(ListView):
    model = Idee
    template_name = "ppale/liste_idees.html"
    context_object_name = "ideas"
    
    
class IdDetailView(DetailView):
    model = Idee
    template_name = "ppale/idee_detail.html"
    context_object_name = "id"
    
# def vote(request, id_user):                                                    #donne la possibilité d'ajouter une note, fonctionalité disponible à partir de la liste de tous les rendez_vous
#     ki_vote= Idee.objects.filter(id=id_user)
    
#     if request.method == 'POST':
#         form = Voter(request.POST)
#         if form.is_valid():
#             form.cleaned_data['client'] = user                                         #la note est assignée au client pour lequel le coach veut ajouter une note
#             form.save()
#             return redirect('list_all_rdv')
#     else:
#         form = Voter()
#     return render(request, 'rendez_vous/add_note.html', {'form': form, 'client':user})

def vote(request, id_user):
    user=request.user
    id_user=id_user
    print(id_user)
    if request.method == 'POST':
        form = Voter(request.POST)
        # form.votant=user
        # form.idee=id_user
        
        if form.is_valid():
            # voti=form.save(commit=False)
            form.cleaned_data['type_vote'] = type                                       #la note est assignée au client pour lequel le coach veut ajouter une note
            # voti=form
            # voti.votant=user
            # voti.idee=id_user
            # v.save()
            form.save()
            # form.save()
            # vote=Votant(votant=user,idee=id_user, type_vote=type )
            return redirect ('liste_ideas')
    else:
        form = Voter()
   
    return render (request, 'ppale/vote.html', {'user':user, 'form':form, 'id_user':id_user})
    
def creer_idee(request):
    if request.method == 'POST':
        form = Idea(request.POST)
        if form.is_valid():
            creer=form.save(commit=False)
            creer.auteur = request.user  
            creer.save()          
            return redirect ('liste_ideas')
    else:
        form = Idea()
    return render (request, 'ppale/creer_idees.html', {'form':form})


def add_note(request, nom_user_rdv):                                                    #donne la possibilité d'ajouter une note, fonctionalité disponible à partir de la liste de tous les rendez_vous
   
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
    
    users = User.objects.filter(username=nom_client)    
    
    # existing_appointments = Appointment.objects.filter(day=day, time=time)     #reprend tous les champs jour et heure des "objets" appointement
     #       if existing_appointments.exists():                                         #si la date et heure sélectionnée correspondent à un rdv déjà pris: message d'erreur et pas d'enregistrement rdv
                #messages.error(request, "Il existe déjà un rendez-vous à cette date et à cette heure")
                
                
# def idees_popu(request):
#     vot=Votant.objects.all()
#     for i in vot:
#         j= i.votant_id
#         z=i.type_vote
#         a=Votant.objects.filter(id=j)
#         print(a)
#         a.score+=z
#     return render (request, 'ppale/idees_popu.html', {'vot':vot})


def idees_popu(request):
    votants=Votant.objects.all()
    ides=Idee.objects.all()
    idees = Idee.objects.order_by('-score')
    for votant in votants:
        idi=votant.idee.id
        print(Idee)
        a=Idee.objects.filter(id=idi)
        print(a)
        
        if votant.type_vote:
            a.update(score=F('score')+1)
        else:
            a.update(score=F('score')-1)
        
        # a.save()
    return render(request, 'ppale/idees_popu.html', {'votants': votants, 'idee':idees})
            
                