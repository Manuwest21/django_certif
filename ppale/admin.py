from django.contrib import admin
from .models import Idee, Votant,UserSelection

# Register your models here.
admin.site.register(Idee)
admin.site.register(Votant)
admin.site.register(UserSelection)