# Generated by Django 4.1.7 on 2024-05-21 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ppale', '0003_idee_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legume', models.CharField(blank=True, choices=[('tomate', 'Tomate'), ('epinard', 'Epinard'), ('concombre', 'Concombre')], max_length=100)),
                ('viande', models.CharField(blank=True, choices=[('boeuf', 'Boeuf'), ('poulet', 'Poulet'), ('poisson', 'Poisson')], max_length=100)),
                ('feculent', models.CharField(blank=True, choices=[('riz', 'Riz'), ('pomme_de_terre', 'Pomme de terre'), ('pates', 'Pâtes')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
