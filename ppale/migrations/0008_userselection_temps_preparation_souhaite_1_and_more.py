# Generated by Django 4.1.7 on 2024-09-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ppale", "0007_userselection_choix_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="userselection",
            name="temps_preparation_souhaite_1",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="userselection",
            name="temps_preparation_souhaite_2",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="userselection",
            name="temps_preparation_souhaite_3",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="userselection",
            name="choix_user",
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
