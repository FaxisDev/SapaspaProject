# Generated by Django 4.2.7 on 2023-12-16 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recibos', '0003_tipopago_remove_recibo_adeudo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipopago',
            options={'verbose_name': 'Tipo de pago', 'verbose_name_plural': 'Tipos de pagos'},
        ),
    ]
