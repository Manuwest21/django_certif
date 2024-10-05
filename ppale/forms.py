from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, get_user_model
from authenti.models import User
from.models import models, Votant, Idee,  UserSelection, Prepa, Role
from django import forms
from django.forms import ModelForm

User = get_user_model()

# class Voter(ModelForm):
   
#     class Meta:
#         model = Votant
#         fields = ['type_vote']
class prepa_form(forms.ModelForm):
    class Meta:
        model = Prepa
        fields = '__all__'

    # Ajoutez un champ de sélection pour les temps de préparation
    choix_temps_preparation = forms.ChoiceField(
        choices=[],  # Les choix seront définis dans la méthode __init__
        required=False,
        label='Choisissez un temps de préparation'
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Récupérez l'utilisateur de kwargs
        super(prepa_form, self).__init__(*args, **kwargs)

        if user:
            # Ajoutez les temps de préparation de l'utilisateur dans le champ de sélection
            temps_choices = []
            if user.temps_preparation_1:
                temps_choices.append((user.temps_preparation_1, user.temps_preparation_1))
            if user.temps_preparation_2:
                temps_choices.append((user.temps_preparation_2, user.temps_preparation_2))
            if user.temps_preparation_3:
                temps_choices.append((user.temps_preparation_3, user.temps_preparation_3))

            # Ajoutez une option vide pour inciter à faire un choix
            temps_choices.insert(0, ('', 'Sélectionnez un temps de préparation'))

            # Mettre à jour les choix du champ de sélection
            self.fields['choix_temps_preparation'].choices = temps_choices

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
            'poisson': forms.Select(choices=UserSelection.poisson_choices),
            'type_repas': forms.Select(choices=UserSelection.repas_choices),
            'temps_préparation_souhaité': forms.Select(choices=UserSelection.temps_choices)
            
        }

    @classmethod
    def with_user(cls, user, *args, **kwargs):
        form = cls(*args, **kwargs)
        print(user.temps_preparation_1, user.temps_preparation_2, user.temps_preparation_3)  # Debug
        if user:
            temps_choices = []
            print(user.temps_preparation_1, user.temps_preparation_2, user.temps_preparation_3)  # Debug
            if user.temps_preparation_1:
                temps_choices.append((user.temps_preparation_1, user.temps_preparation_1))
            if user.temps_preparation_2:
                temps_choices.append((user.temps_preparation_2, user.temps_preparation_2))
            if user.temps_preparation_3:
                temps_choices.append((user.temps_preparation_3, user.temps_preparation_3))

            temps_choices.insert(0, ('', 'Sélectionnez un temps de préparation'))

            form.fields['choix_user'] = forms.Select(
                choices=temps_choices,
                required=False,
                label='Choix de temps de préparation',
            )
        return form
                    






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


class CustomUserCreationForm(UserCreationForm):
    # Champs personnalisés pour les temps de préparation habituels
    temps_preparation_1 = forms.CharField(
        max_length=20,
        required=False,
        label="Temps de préparation 1",
        widget=forms.TextInput(attrs={'placeholder': 'Temps de préparation 1 (max 20 caractères)'}),
    )
    temps_preparation_2 = forms.CharField(
        max_length=20,
        required=False,
        label="Temps de préparation 2",
        widget=forms.TextInput(attrs={'placeholder': 'Temps de préparation 2 (max 20 caractères)'}),
    )
    temps_preparation_3 = forms.CharField(
        max_length=20,
        required=False,
        label="Temps de préparation 3",
        widget=forms.TextInput(attrs={'placeholder': 'Temps de préparation 3 (max 20 caractères)'}),
    )
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        required=False,
        label="Choisissez un rôle",
        empty_label="Sélectionnez un rôle")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'temps_preparation_1', 'temps_preparation_2', 'temps_preparation_3']


# forms.py


class MetricsForm(forms.Form):      
    METRICS_CHOICES = [           # Ajout des métriques que l'on veut proposer en choix de visuel pour l'administrateur
        ('django_http_responses_total_by_status_view_method_total', 'Total des réponses par statut et méthode de vue'),
        ('django_http_responses_body_total_bytes', 'Total des octets du corps des réponses'),
        ('django_http_responses_total_by_charset_total', 'Total des réponses par charset'),
        ('django_http_responses_streaming_total', 'Total des réponses en streaming'),
        ('django_http_exceptions_total_by_view_total', 'Total des exceptions par vue'),
        
    ]

    selected_metrics = forms.MultipleChoiceField(
        choices=METRICS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Sélectionnez les métriques que vous voulez afficher"
    )