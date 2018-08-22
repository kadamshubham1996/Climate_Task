# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region', models.CharField(max_length=50)),
                ('Climate_type', models.CharField(choices=[(b'Max_Temp', b'Max_Temp'), (b'Min_Temp', b'Min_Temp'), (b'Mean_Temp', b'Mean_Temp'), (b'Sunshine', b'Sunshine'), (b'Rainfall', b'Rainfall'), (b'Raindays', b'Raindays'), (b'Days_of_Air_frost', b'Days_of_Air_frost')], default=None, max_length=124)),
                ('Year', models.CharField(max_length=50, null=True)),
                ('Jan', models.CharField(max_length=50, null=True)),
                ('Feb', models.CharField(max_length=50, null=True)),
                ('Mar', models.CharField(max_length=50, null=True)),
                ('Apr', models.CharField(max_length=50, null=True)),
                ('May', models.CharField(max_length=50, null=True)),
                ('Jun', models.CharField(max_length=50, null=True)),
                ('Jul', models.CharField(max_length=50, null=True)),
                ('Aug', models.CharField(max_length=50, null=True)),
                ('Sep', models.CharField(max_length=50, null=True)),
                ('Oct', models.CharField(max_length=50, null=True)),
                ('Nov', models.CharField(max_length=50, null=True)),
                ('Dec', models.CharField(max_length=50, null=True)),
                ('Win', models.CharField(max_length=50, null=True)),
                ('Spr', models.CharField(max_length=50, null=True)),
                ('Sum', models.CharField(max_length=50, null=True)),
                ('Aut', models.CharField(max_length=50, null=True)),
                ('Ann', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
