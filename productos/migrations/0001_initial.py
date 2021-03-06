# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.IntegerField(default=0)),
                ('producto_foto', models.CharField(max_length=1000)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Categoria')),
            ],
        ),
    ]
