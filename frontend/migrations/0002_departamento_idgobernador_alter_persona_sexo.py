# Generated by Django 5.0.3 on 2024-04-07 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='idGobernador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='frontend.persona'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No especificado')], default='N', max_length=1),
        ),
    ]
