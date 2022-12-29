# -*- coding: utf-8 -*-
"""
@File        : base.py
@Author      : Lu Wei
@Time        : 2022/12/29 10:52 上午
@Description :
"""
from django.db import models


class AtBaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="数据更新时间"
    )

    class Meta:
        verbose_name = "带有时间的属性的基础模型"
        abstract = True


class SimpleNameAndCodeNameModel(models.Model):
    """抽象类"""
    name = models.CharField(
        max_length=200,
        verbose_name="中文名字"
    )
    code_name = models.CharField(
        max_length=200,
        verbose_name="英文代码"
    )

    class Meta:
        abstract = True
