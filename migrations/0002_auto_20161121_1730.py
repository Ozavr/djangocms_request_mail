# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestlist',
            options={'verbose_name': 'Список запросов', 'verbose_name_plural': 'Список запросов', 'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='requestlist',
            name='description',
            field=models.TextField(verbose_name='Краткое содержание вашей заявки', blank=True, max_length=350),
        ),
    ]
