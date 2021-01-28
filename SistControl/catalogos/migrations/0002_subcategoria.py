# Generated by Django 2.2.12 on 2020-09-29 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('modificador', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(help_text='Nombre subcategoría', max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Categorias')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'subcategoría',
                'verbose_name_plural': 'subcategorías',
                'ordering': ['nombre'],
                'unique_together': {('categoria', 'nombre')},
            },
        ),
    ]
