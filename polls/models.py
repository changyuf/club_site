# -*- coding:utf8 -*-
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="问题内容")
    pub_date = models.DateTimeField('发布日期')

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "问题"
        #app_label = 'myapp'

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "选择"
        verbose_name_plural = "选择"

    def __unicode__(self):
        return self.choice_text



