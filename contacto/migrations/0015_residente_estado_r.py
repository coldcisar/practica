# Generated by Django 3.2.8 on 2023-06-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0014_alter_propietario_telefono_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='residente',
            name='estado_r',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
