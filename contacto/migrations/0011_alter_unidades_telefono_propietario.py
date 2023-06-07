# Generated by Django 3.2.8 on 2023-06-01 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0010_rename_telefono_propetario_propietario_telefono_propietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidades',
            name='telefono_propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefono_propietario', to='contacto.id_propietario'),
        ),
    ]
