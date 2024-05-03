# Generated by Django 3.1 on 2023-11-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Propiedades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField(default=None)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de Propiedad',
                'verbose_name_plural': 'Tipo de Propiedades',
            },
        ),
        migrations.AlterModelOptions(
            name='propiedad',
            options={'verbose_name': 'Propiedad', 'verbose_name_plural': 'Propiedades'},
        ),
    ]