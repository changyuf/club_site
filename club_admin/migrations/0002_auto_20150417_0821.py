# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_admin', '0001_initial'),
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=300)),
                ('activity_position', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('cost_male', models.IntegerField(default=0)),
                ('cost_female', models.IntegerField(default=0)),
                ('max_participants', models.IntegerField(default=0)),
                ('dead_line', models.DateTimeField()),
                ('organiser', models.CharField(max_length=100)),
                ('organiser_phone', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'activity',
            },
            bases=(models.Model,),
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
            },
            bases=(models.Model,),
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
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('activity', 'account_id')]),
        ),
    ]
