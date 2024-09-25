from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
)
  
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    birth_date= models.DateField (auto_now=False, null=True)    #auto_now: par défault mettre date de maintennat!
    email = models.EmailField(unique=True)
    temps_preparation_1 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Temps de préparation 1')
    temps_preparation_2 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Temps de préparation 2')
    temps_preparation_3 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Temps de préparation 3')

    # Méthode de représentation
    def __str__(self):
        return self.username
    
    
    
    
