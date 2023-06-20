# Generated by Django 3.2.8 on 2023-06-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0015_residente_estado_r'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidades',
            name='tipo_comunidades',
            field=models.CharField(choices=[('Condominio', 'Condiminio'), ('Edificio', 'Edificio'), ('Loteo', 'Loteo'), ('Villa', 'Villa')], default='Condominio', max_length=20, null=True),
        ),
    ]