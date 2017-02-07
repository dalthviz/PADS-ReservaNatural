# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_usuario_imagefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Pais'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Ciudad'),
        ),
    ]