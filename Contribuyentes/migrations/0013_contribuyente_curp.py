# Generated by Django 4.2.7 on 2024-03-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contribuyentes', '0012_contribuyente_folio_unico'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribuyente',
            name='curp',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
    ]
