# Generated by Django 5.0.3 on 2024-04-12 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0002_tipovivienda_vivienda_persona_idvivienda'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoVivienda',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='idVivienda',
        ),
        migrations.DeleteModel(
            name='Vivienda',
        ),
    ]
