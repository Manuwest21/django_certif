# Generated by Django 4.1.7 on 2024-09-25 22:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ppale", "0012_alter_idee_auteur_alter_prepa_votant_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="role",
            table="préférence",
        ),
    ]
