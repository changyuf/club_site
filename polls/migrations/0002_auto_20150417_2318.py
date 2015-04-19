# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '\u9009\u62e9', 'verbose_name_plural': '\u9009\u62e9'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u95ee\u9898', 'verbose_name_plural': '\u95ee\u9898'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='quest_text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=datetime.datetime(2015, 4, 17, 15, 18, 39, 916000, tzinfo=utc), max_length=200, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=False,
        ),
    ]
