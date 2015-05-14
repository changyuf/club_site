# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QQAccount',
            fields=[
                ('uin', models.CharField(max_length=40)),
                ('qq', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('nick_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('balance', models.IntegerField(default=0)),
                ('club_level', models.IntegerField(default=0)),
                ('activity_times', models.IntegerField(default=0)),
                ('accumulate_points', models.IntegerField(default=0)),
                ('card', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
                ('other_comments', models.CharField(max_length=200)),
                ('weixin_id', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'qq_account',
            },
            bases=(models.Model,),
        ),
    ]
