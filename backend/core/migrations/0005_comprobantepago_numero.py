# Generated by Django 5.1.4 on 2025-04-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_factura_ordentrabajo_factura_cotizacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobantepago',
            name='numero',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
