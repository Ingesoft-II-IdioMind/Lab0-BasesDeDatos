# Generated by Django 5.0.3 on 2024-04-12 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Barrio', '0002_barrio_idmunicipio_alter_barrio_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barrio',
            old_name='nombre',
            new_name='nombreBarrio',
        ),
    ]