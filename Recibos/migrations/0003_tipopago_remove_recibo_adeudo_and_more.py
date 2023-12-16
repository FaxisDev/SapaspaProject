# Generated by Django 4.2.7 on 2023-12-16 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recibos', '0002_alter_recibo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de pago',
                'verbose_name_plural': 'Tipo de pagos',
            },
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='adeudo',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='mes_pago',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='sub_total',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='total',
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('adeudo', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('mes_pago', models.DateField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('tipo_pago', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='Recibos.tipopago')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.AddField(
            model_name='recibo',
            name='pago',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='Recibos.pago'),
        ),
    ]
