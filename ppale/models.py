from django.db import models
from authenti.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Idee(models.Model):

    class affection (models.TextChoices):
        trop_passione = ' 5/5'
        moyen_passione = '3/5'
        faible_passione = '1.5/5'
        NA = 'NA'

    formulation = models.CharField(max_length=100)
    detail = models.CharField(max_length=200, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=100, blank=True)
    vues_recentes = models.IntegerField (default=0,
    validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    

    affection= models.fields.CharField(default='NC',choices=affection.choices, max_length=25)
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

class bets_faits(models.Model):        
    nom_bet = models.CharField(max_length=200, null=True)
    type_pari = models.CharField(max_length=200, null=True)
    côte = models.IntegerField(default=100, blank=True)
    confiance= models.CharField(max_length=200, null=True)
    résultat=models.CharField(max_length=200, null=True)


