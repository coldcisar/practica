# Generated by Django 3.2.8 on 2023-05-30 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0006_auto_20230529_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='id_propietario',
            options={'verbose_name': 'id_propietario', 'verbose_name_plural': 'id_propietarios'},
        ),
        migrations.AlterModelOptions(
            name='id_residente',
            options={'verbose_name': 'id_residente', 'verbose_name_plural': 'id_residentes'},
        ),
    ]
