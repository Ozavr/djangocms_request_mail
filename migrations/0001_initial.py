# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('description', models.TextField(max_length=350, verbose_name='Содержание запроса')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Список запросов',
                'ordering': ['-date'],
            },
        ),
    ]
