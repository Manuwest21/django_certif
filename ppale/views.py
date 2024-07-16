from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from.models import Idee, Votant,  UserSelection
from . import forms
from .forms import Voter, Idea, aliments
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import F

import os
# from openai import OpenAI
from dotenv import load_dotenv
# Create your views here.
import os
import openai
# from openai import AzureOpenAI

from azure.identity import DefaultAzureCredential, get_bearer_token_provider


load_dotenv()
openai.api_type="azure"
openai.api_base="https://django.openai.azure.com/"
openai.api_version="2024-02-01"
openai.api_key=os.getenv("OPENAI_API_KEY")
deployment_name="django3"
# endpoint = os.getenv["https://django.openai.azure.com/"]

# deployment = os.getenv["CHAT_COMPLETIONS_DEPLOYMENT_NAME"]

# search_endpoint = os.getenv["SEARCH_ENDPOINT"]

# search_index = os.environ["SEARCH_INDEX"]

      

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")

      

# client = AzureOpenAI(

#     azure_endpoint=endpoint,

#     azure_ad_token_provider=token_provider,

#     api_version="2024-02-01",

# )

# client = OpenAI (api_key=os.getenv("open_ai_key"))

# client = OpenAI (api_key='sk-proj-18fEAPYKQaYAm5Mt0Kc4T3BlbkFJ6tyvsnXi9GQTVz1ehpAr')
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
            
# openai = os.getenv('open_ai_key')               

# def aliments(request, id_user):
def aliments_views(request):
    user=request.user
    # id_user=id_user
    # print(id_user)
    if request.method == 'POST':
        form = aliments(request.POST)
        # form.votant=user
        # form.idee=id_user
        
        if form.is_valid():
            # voti=form.save(commit=False)
            form.cleaned_data['type_vote'] = type                                       #la note est assignée au client pour lequel le coach veut ajouter une note
            # voti=form
            # voti.votant=user
            # voti.idee=id_user
            user_selection = form.save(commit=False)
            user_selection.user = user
            user_selection.save()
            selections = {
                'legume': user_selection.legume,
                'viande': user_selection.viande,
                'feculent': user_selection.feculent,
            }
            prompt = f"L'utilisateur a sélectionné les ingrédients suivants: Légume: {selections['legume']}, Viande: {selections['viande']}, Féculent: {selections['feculent']}."

            # Appeler l'API OpenAI
            api_key = os.getenv('open_ai_key')
            response = requests.post(
                'https://api.openai.com/v1/engines/davinci-codex/completions',
                headers={'Authorization': f'Bearer {api_key}'},
                json={
                    'prompt': prompt,
                    'max_tokens': 150
                }
            )

            # Vérifier la réponse de l'API
            if response.status_code == 200:
                api_response = response.json()
                chatgpt_response = api_response['choices'][0]['text']
                return render(request, 'ppale/response.html', {'response': chatgpt_response})
            else:
                return render(request, 'ppale/error.html', {'message': 'Failed to get response from API.'})
            # v.save()
            form.save()
            # form.save()
            # vote=Votant(votant=user,idee=id_user, type_vote=type )
            return redirect ('liste_ideas')
    else:
        form =aliments()
   
    # return render (request, 'ppale/aliments.html', {'user':user, 'form':form, 'id_user':id_user})
    return render (request, 'ppale/aliments.html', {'user':user, 'form':form})


def aliments_view11(request):
    user = request.user
    if request.method == 'POST':
        form = aliments(request.POST)
        if form.is_valid():
            user_selection = form.save(commit=False)
            user_selection.user = user
            user_selection.save()
            
            # Récupérer les sélections de l'utilisateur
            selections = {
                'legume': user_selection.legume,
                'viande': user_selection.viande,
                'feculent': user_selection.feculent,
                'poisson':user_selection.poisson,
                'temps_préparation_souhaité':user_selection.temps_souhaite,
                'repas_souhaite':user_selection.repas_souhaite,
            }
            
            # Préparer les données pour l'API
            prompt = f"L'utilisateur a sélectionné les ingrédients suivants: Légume: {selections['legume']}, Viande: {selections['viande']}, Féculent: {selections['feculent']}, Poisson:{selections['poisson']}, il veut une recette de repas à partir de ces ingrédients de base ici pour un repas de type :{selections['repas_souhaite']} et avec un temps de préparation de :{selections['temps_préparation_souhaité']}  ."

            # try:
                # Appeler l'API OpenAI avec le modèle "gpt-3.5-turbo"
                # response = openai.ChatCompletion.create(
                #     model="gpt-3.5-turbo",
                #     messages=[
                #         {"role": "system", "content": "You are a culinary assistant, skilled in creating recipes based on selected ingredients."},
                #         {"role": "user", "content": prompt}
                #     ]
                # )
            response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    seed=17,
                    #temperature=1,   # 0 <-> 1 NOT USE WITH TOP-P : What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
                    max_tokens=2000,   # max 4096 tokens output
                    top_p= 1,         # % sur une echelle de 0 a 1. NOT USE WITH TEMPERATURE  : An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
                    frequency_penalty= 0.2, # -2 <-> 2 Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line
                    presence_penalty= 0.2,   # -2 <-> 2 Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics


                    messages=[ {"role": "system", "content": " You are a culinary assistant, skilled in creating recipes based on selected ingredients."},
                                {"role": "user", "content": "prompt "}]
                            
                                        
                            )
            
            # Vérifier la réponse de l'API
            if response and response.choices:
                answer = response.choices[0].message.content
                # print(f"Réponse générée par le modèle: {answer}")
                # return answer
                return render(request, 'ppale/response.html', {'response': answer})
            else:
                return render(request, 'ppale/error.html', {'message': 'No response from API.'})
        # except openai.error.OpenAIError as e:
        #     return render(request, 'ppale/error.html', {'message': f"OpenAI API error:là"})
    else:
        form = aliments()

    return render(request, 'ppale/aliments.html', {'user': user, 'form': form})

deployment_id = os.getenv("CHAT_COMPLETIONS_DEPLOYMENT_NAME")

def aliments_view(request):
    user = request.user
    if request.method == 'POST':
        form = aliments(request.POST)
        if form.is_valid():
            user_selection = form.save(commit=False)
            user_selection.user = user
            user_selection.save()
            
            # Récupérer les sélections de l'utilisateur
            selections = {
                'legume': user_selection.legume,
                'viande': user_selection.viande,
                'feculent': user_selection.feculent,
                'poisson': user_selection.poisson,
                'temps_préparation_souhaité': user_selection.temps_souhaite,
                'repas_souhaite': user_selection.repas_souhaite,
            }
            prompt1 = (
    f"donne moi une recette, L'utilisateur a sélectionné les ingrédients suivants : "
    f"Légume: {selections['legume']}, Viande: {selections['viande']}, "
    f"Féculent: {selections['feculent']}, Poisson: {selections['poisson']}, "
    
    f"et 30min max de préparation."
)
            messages = [
             {
              "role": "user",
              "content": prompt1
                 },      
                {
              "role": "assistant",
             "content": "Je peux vous proposer une recette avec ces ingrédients. Veuillez patienter un moment pendant que je génère la recette..."
    }
]
            # Préparer les données pour l'API
            # prompt1 = (f"L'utilisateur a sélectionné les ingrédients suivants: "
            #           f"Légume: {selections['legume']}, Viande: {selections['viande']}, "
            #           f"Féculent: {selections['feculent']}, Poisson: {selections['poisson']}, "
            #           f"il veut une recette de repas à partir de ces ingrédients de base ici pour un repas de type : "
            #           f"{selections['repas_souhaite']} et avec un temps de préparation de : "
            #           f"{selections['temps_préparation_souhaité']}.")

           
            response = openai.ChatCompletion.create(
                        engine=deployment_name,
                        messages=messages,
                        max_tokens=500,
                        temperature=0.7,
                        top_p=0.95,
                        frequency_penalty=0,
                        presence_penalty=0
)

# Extract and print the response
            text = response['choices'][0]['message']['content'].replace('\n', '').replace(' .', '.').strip()
            print(text)

            if response :
            #    text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
               return render(request, 'ppale/response.html', {'response': text})
            else:
                return render(request, 'ppale/error.html', {'message': 'No response from API.'})
            

    else:
        form = aliments()

    return render(request, 'ppale/aliments.html', {'user': user, 'form': form})


