# Generated by Django 5.0.3 on 2024-03-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_alter_departamento_idgobernador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nombreDepartamento',
            field=models.CharField(default='no name', max_length=45),
        ),
    ]
