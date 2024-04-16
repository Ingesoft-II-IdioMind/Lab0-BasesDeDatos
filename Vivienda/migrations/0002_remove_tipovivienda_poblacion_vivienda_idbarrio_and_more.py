# Generated by Django 5.0.3 on 2024-04-12 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barrio', '0003_rename_nombre_barrio_nombrebarrio'),
        ('Vivienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipovivienda',
            name='poblacion',
        ),
        migrations.AddField(
            model_name='vivienda',
            name='idBarrio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Barrio.barrio'),
        ),
        migrations.AddField(
            model_name='vivienda',
            name='idTipo_vivienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Vivienda.tipovivienda'),
        ),
        migrations.AlterField(
            model_name='tipovivienda',
            name='nombre',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='direccion',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]