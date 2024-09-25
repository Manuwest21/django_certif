# Generated by Django 4.1.7 on 2024-09-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authenti", "0002_remove_user_profile_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="temps_preparation_1",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Temps de préparation 1",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="temps_preparation_2",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Temps de préparation 2",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="temps_preparation_3",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Temps de préparation 3",
            ),
        ),
    ]
