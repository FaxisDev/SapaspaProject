# Generated by Django 3.1 on 2023-11-14 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Contribuyentes', '0002_auto_20231113_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribuyente',
            name='id_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
