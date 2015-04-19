# -*- coding:utf8 -*-
from django.db import models

# Create your models here.


class QQAccount(models.Model):
    uin = models.CharField(max_length=40)
    qq = models.CharField(max_length=40, primary_key=True, verbose_name='QQ号')
    nick_name = models.CharField(max_length=100, verbose_name='昵称')
    gender = models.CharField(max_length=10, verbose_name='性别')
    balance = models.IntegerField(default=0, verbose_name='余额')
    club_level = models.IntegerField(default=0, verbose_name='等级')
    activity_times = models.IntegerField(default=0, verbose_name='参加活动次数')
    accumulate_points = models.IntegerField(default=0, verbose_name='积分')
    card = models.CharField(max_length=200, verbose_name='群名片')
    comments = models.CharField(max_length=200, null=True, verbose_name='自我评价')
    other_comments = models.CharField(max_length=200, null=True, verbose_name='别人评价')
    weixin_id = models.CharField(max_length=200, null=True, verbose_name='微信ID')

    class Meta:
        db_table = "qq_account"
        verbose_name = "俱乐部QQ会员"
        verbose_name_plural = "俱乐部QQ会员"


class Activity(models.Model):
    title = models.CharField(max_length=200, verbose_name='活动名称')
    description = models.CharField(max_length=300, null=True, verbose_name='活动描述')
    activity_position = models.CharField(max_length=100, verbose_name='活动地点')
    start_time = models.DateTimeField(verbose_name='开始时间')
    stop_time = models.DateTimeField(verbose_name='结束时间')
    cost_male = models.IntegerField(default=0, verbose_name='活动费用（男）')
    cost_female = models.IntegerField(default=0, verbose_name='活动费用（女）')
    max_participants = models.IntegerField(default=0, verbose_name='最大人数')
    dead_line = models.DateTimeField(verbose_name='报名截至时间')
    organiser = models.CharField(max_length=100, verbose_name='组织者')
    organiser_phone  = models.CharField(max_length=100, verbose_name='组织者电话')

    class Meta:
        db_table = "activity"
        verbose_name = "活动"
        verbose_name_plural = "活动"


class Participant(models.Model):
    activity = models.ForeignKey(Activity)
    account_type = models.CharField(max_length=20)
    account_id = models.CharField(max_length=100)
    account_name = models.CharField(max_length=200)
    account_gender = models.CharField(max_length=10)
    add_on_female = models.IntegerField(default=0)
    add_on_male = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)

    class Meta:
        db_table = "participant"
        unique_together = ("activity", "account_id")
        verbose_name = "活动报名"
        verbose_name_plural = "活动报名"


class BillDetails(models.Model):
    account_type = models.CharField(max_length=20)
    account_id = models.CharField(max_length=100)
    account_name = models.CharField(max_length=200)
    operator = models.CharField(max_length=200)
    operate_time = models.DateTimeField()
    balance_change = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    comments = models.CharField(max_length=200, default="")

    class Meta:
        db_table = "bill_details"
        verbose_name = "会费详单"
        verbose_name_plural = "会费详单"


class AccumulatePointDetails(models.Model):
    account_type = models.CharField(max_length=20)
    account_id = models.CharField(max_length=100)
    account_name = models.CharField(max_length=200)
    operate_time = models.DateTimeField()
    points_change = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    comments = models.CharField(max_length=200, default="")

    class Meta:
        db_table = "accumulate_points_details"
        verbose_name = "积分详单"
        verbose_name_plural = "积分详单"
