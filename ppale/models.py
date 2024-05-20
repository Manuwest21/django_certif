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