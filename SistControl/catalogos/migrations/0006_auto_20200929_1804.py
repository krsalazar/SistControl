# Generated by Django 2.2.12 on 2020-09-30 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0005_productos'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productos',
            unique_together={('codigo', 'codigo_barra')},
        ),
    ]
