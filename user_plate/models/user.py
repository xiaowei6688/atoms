# -*- coding: utf-8 -*-
"""
@File        : user.py
@Author      : Lu Wei
@Time        : 2022/12/29 10:46 上午
@Description :
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.const import USER_APP_LABEL


class AtomUser(AbstractUser):
    personal_token = models.CharField(
        unique=True,
        max_length=255,
        null=True,
        verbose_name="个人密钥"
    )
    phone = models.CharField(
        unique=True,
        db_index=True,
        max_length=11,
        verbose_name="手机号"
    )
    email = models.CharField(
        unique=True,
        max_length=100,
        verbose_name="邮箱"
    )
    nick_name = models.CharField(
        max_length=30,
        verbose_name="昵称"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="最后更新时间"
    )

    class Meta:
        db_table = "atom_user"
        verbose_name = "用户表"
        app_label = USER_APP_LABEL
