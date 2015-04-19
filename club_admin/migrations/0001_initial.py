# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccumulatePointDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=20)),
                ('account_id', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=200)),
                ('operate_time', models.DateTimeField()),
                ('points_change', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('comments', models.CharField(default=b'', max_length=200)),
            ],
            options={
                'db_table': 'accumulate_points_details',
                'verbose_name': '\u79ef\u5206\u8be6\u5355',
                'verbose_name_plural': '\u79ef\u5206\u8be6\u5355',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.CharField(max_length=300, null=True, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('activity_position', models.CharField(max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x9c\xb0\xe7\x82\xb9')),
                ('start_time', models.DateTimeField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('stop_time', models.DateTimeField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('cost_male', models.IntegerField(default=0, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe8\xb4\xb9\xe7\x94\xa8\xef\xbc\x88\xe7\x94\xb7\xef\xbc\x89')),
                ('cost_female', models.IntegerField(default=0, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe8\xb4\xb9\xe7\x94\xa8\xef\xbc\x88\xe5\xa5\xb3\xef\xbc\x89')),
                ('max_participants', models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x80\xe5\xa4\xa7\xe4\xba\xba\xe6\x95\xb0')),
                ('dead_line', models.DateTimeField(verbose_name=b'\xe6\x8a\xa5\xe5\x90\x8d\xe6\x88\xaa\xe8\x87\xb3\xe6\x97\xb6\xe9\x97\xb4')),
                ('organiser', models.CharField(max_length=100, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe8\x80\x85')),
                ('organiser_phone', models.CharField(max_length=100, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe8\x80\x85\xe7\x94\xb5\xe8\xaf\x9d')),
            ],
            options={
                'db_table': 'activity',
                'verbose_name': '\u6d3b\u52a8',
                'verbose_name_plural': '\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=20)),
                ('account_id', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=200)),
                ('operator', models.CharField(max_length=200)),
                ('operate_time', models.DateTimeField()),
                ('balance_change', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('comments', models.CharField(default=b'', max_length=200)),
            ],
            options={
                'db_table': 'bill_details',
                'verbose_name': '\u4f1a\u8d39\u8be6\u5355',
                'verbose_name_plural': '\u4f1a\u8d39\u8be6\u5355',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=20)),
                ('account_id', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=200)),
                ('account_gender', models.CharField(max_length=10)),
                ('add_on_female', models.IntegerField(default=0)),
                ('add_on_male', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('activity', models.ForeignKey(to='club_admin.Activity')),
            ],
            options={
                'db_table': 'participant',
                'verbose_name': '\u6d3b\u52a8\u62a5\u540d',
                'verbose_name_plural': '\u6d3b\u52a8\u62a5\u540d',
            },
        ),
        migrations.CreateModel(
            name='QQAccount',
            fields=[
                ('uin', models.CharField(max_length=40)),
                ('qq', models.CharField(max_length=40, serialize=False, verbose_name=b'QQ\xe5\x8f\xb7', primary_key=True)),
                ('nick_name', models.CharField(max_length=100, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('gender', models.CharField(max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('balance', models.IntegerField(default=0, verbose_name=b'\xe4\xbd\x99\xe9\xa2\x9d')),
                ('club_level', models.IntegerField(default=0, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7')),
                ('activity_times', models.IntegerField(default=0, verbose_name=b'\xe5\x8f\x82\xe5\x8a\xa0\xe6\xb4\xbb\xe5\x8a\xa8\xe6\xac\xa1\xe6\x95\xb0')),
                ('accumulate_points', models.IntegerField(default=0, verbose_name=b'\xe7\xa7\xaf\xe5\x88\x86')),
                ('card', models.CharField(max_length=200, verbose_name=b'\xe7\xbe\xa4\xe5\x90\x8d\xe7\x89\x87')),
                ('comments', models.CharField(max_length=200, null=True, verbose_name=b'\xe8\x87\xaa\xe6\x88\x91\xe8\xaf\x84\xe4\xbb\xb7')),
                ('other_comments', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x88\xab\xe4\xba\xba\xe8\xaf\x84\xe4\xbb\xb7')),
                ('weixin_id', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1ID')),
            ],
            options={
                'db_table': 'qq_account',
                'verbose_name': '\u4ff1\u4e50\u90e8QQ\u4f1a\u5458',
                'verbose_name_plural': '\u4ff1\u4e50\u90e8QQ\u4f1a\u5458',
            },
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('activity', 'account_id')]),
        ),
    ]
