# Generated by Django 4.2.7 on 2024-08-04 22:21

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('PreguntasFrecuentes', '0002_alter_preguntafrecuente_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntafrecuente',
            name='descripcion',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='descripcion'),
        ),
    ]