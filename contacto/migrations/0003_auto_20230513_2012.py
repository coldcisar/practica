# Generated by Django 3.2.8 on 2023-05-14 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_auto_20230513_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='nuevoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=150)),
                ('contraseña', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]