from django.db import models
from authenti.models import User


# Create your models here.

class Idee(models.Model):
    formulation = models.CharField(max_length=100)
    detail = models.CharField(max_length=200, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=100, blank=True)
    
    def __str__(self):
        return f"{self.formulation} "
    
    class Meta:
        verbose_name_plural = 'Idee'

class Votant(models.Model):
    votant = models.ForeignKey(User, on_delete=models.CASCADE)
    idee = models.ForeignKey(Idee, on_delete=models.CASCADE)
    type_vote = models.BooleanField()
    
    def __str__(self):
        return f"{self.votant} - {self.idee.formulation}"
    
    class Meta:
        verbose_name_plural = 'Votant'


class Votant(models.Model):
    votant = models.ForeignKey(User, on_delete=models.CASCADE)
    idee = models.ForeignKey(Idee, on_delete=models.CASCADE)
    type_vote = models.BooleanField()
    
    def __str__(self):
        return f"{self.votant} - {self.idee.formulation}"
    
    class Meta:
        verbose_name_plural = 'Votant'


# class IngredientsForm(ModelForm):
#     class Meta:
#         model = IngredientsModel
#         fields = ["proteins","vegetables","legumes","starch","spices_and_herbs"]




class UserSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    legume_choices = [
       ('asperge', 'Asperge'),
        ('aubergine', 'Aubergine'),
        ('betterave', 'Betterave'),
        ('brocoli', 'Brocoli'),
        ('carotte', 'Carotte'),
        ('céleri', 'Céleri'),
        ('chou-fleur', 'Chou-fleur'),
        ('chou de Bruxelles', 'Chou de Bruxelles'),
        ('chou rouge', 'Chou rouge'),
        ('concombre', 'Concombre'),
        ('courgette', 'Courgette'),
        ('épinard', 'Épinard'),
        ('fenouil', 'Fenouil'),
        ('haricot vert', 'Haricot vert'),
        ('laitue', 'Laitue'),
        ('navet', 'Navet'),
        ('oignon', 'Oignon'),
        ('poireau', 'Poireau'),
        ('poivron', 'Poivron'),
        ('pomme de terre', 'Pomme de terre'),
        ('radis', 'Radis'),
        ('tomate', 'Tomate')
        # Ajoutez d'autres choix de légumes ici
    ]
    legume = models.CharField(max_length=100, choices=legume_choices, blank=True)

    viande_choices = [
        ('agneau', 'Agneau'),
        ('boeuf', 'Boeuf'),
        ('canard', 'Canard'),
        ('dinde', 'Dinde'),
        ('lapin', 'Lapin'),
        ('porc', 'Porc'),
        ('poulet', 'Poulet'),
        ('veau', 'Veau'),
        # Ajoutez d'autres choix de viandes ici
    ]
    viande = models.CharField(max_length=100, choices=viande_choices, blank=True)

    poisson_choices = [
        ('agneau', 'Agneau'),
        ('boeuf', 'Boeuf'),
        ('canard', 'Canard'),
        ('dinde', 'Dinde'),
        ('lapin', 'Lapin'),
        ('porc', 'Porc'),
        ('poulet', 'Poulet'),
        ('veau', 'Veau'),
        # Ajoutez d'autres choix de viandes ici
    ]
    poisson = models.CharField(max_length=100, choices=poisson_choices, blank=True)


    temps_choices= [
        ('moins de 15min abs', 'moins de 16minutes'),
        ('30 minutes max', 'moins de 31 minutes'),
        ('ok pour longue préparation', 'temps de préparation toléré entre 30minutes et 1h30')

    ]
    temps_souhaite= [ models.CharField(max_length=100, choices=temps_choices, blank=True)]


    repas_choices=[
        ('entree','entree'),
        ('plat', 'plat'),
        ('dessert','dessert')
    ]
    repas_souhaite= [ models.CharField(max_length=100, choices=repas_choices, blank=True)]
    feculent_choices = [
        ('boulgour', 'Boulgour'),
        ('maïs', 'Maïs'),
        ('pain', 'Pain'),
        ('pâtes', 'Pâtes'),
        ('pomme_de_terre', 'Pomme de terre'),
        ('quinoa', 'Quinoa'),
        ('riz', 'Riz'),
        ('semoule', 'Semoule'),
        # Ajoutez d'autres choix de féculents ici
    ]
    feculent = models.CharField(max_length=100, choices=feculent_choices, blank=True)

    # Ajoutez d'autres catégories d'ingrédients avec des listes de choix similaires
    # Par exemple, fruits, produits laitiers, épices, etc.

    def __str__(self):
        return f"Selections of {self.user.username}"
