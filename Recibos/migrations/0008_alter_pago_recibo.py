# Generated by Django 4.2.7 on 2024-07-29 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recibos', '0007_remove_pago_tipo_pago_recibo_tipo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='recibo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Recibos.recibo'),
        ),
    ]
