from django.core.management.base import BaseCommand
from ppale.models import Role

class Command(BaseCommand):
    help = 'Peupler la base de données avec des rôles par défaut'

    def handle(self, *args, **kwargs):
        roles = [
            ('vegetarien', 'généres moi une recette qui répond au critère de repas végétarien'),
            ('sans gluten', 'généres moi une recette qui répond au critère de repas sans gluten'),
            ('repas proteiné', 'généres moi une recette qui répond au critère de repas protéiné'),
        ]
        
        for name, description in roles:
            Role.objects.get_or_create(name=name, description=description)
            self.stdout.write(self.style.SUCCESS(f'Rôle "{name}" ajouté.'))