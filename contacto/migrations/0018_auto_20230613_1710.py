# Generated by Django 3.2.8 on 2023-06-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0017_auto_20230613_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='tipo_unidad',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='residente',
            name='tipo_unidad_residente',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento')], max_length=15, null=True),
        ),
    ]