# -*- coding: utf-8 -*-
"""
@File        : permission.py
@Author      : Lu Wei
@Time        : 2022/12/29 10:59 上午
@Description :
"""
from django.db import models

from common.const import USER_APP_LABEL
from .base import SimpleNameAndCodeNameModel
from .user import AtomUser


class Role(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="角色名称"
    )
    desc = models.CharField(
        max_length=255,
        verbose_name="角色描述",
        null=True
    )
    status = models.BooleanField(
        default=True,
        verbose_name="开启关闭状态"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="创建时间"
    )

    class Meta:
        db_table = "role"
        app_label = USER_APP_LABEL
        verbose_name = "角色表"


class Permission(SimpleNameAndCodeNameModel):

    class Meta:
        db_table = "permission"
        app_label = USER_APP_LABEL
        verbose_name = "权限表"


class UserRole(models.Model):
    user = models.ForeignKey(
        AtomUser,
        related_name="user_roles",
        on_delete=models.CASCADE,
        verbose_name="用户"
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        verbose_name="角色"
    )

    class Meta:
        db_table = "user_role"
        app_label = USER_APP_LABEL
        unique_together = ("role", "user")
        verbose_name = "用户角色映射表"


class RolePermission(models.Model):
    action_choices = (
        ("read", "可查看"),
        ("write", "可编辑")
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        verbose_name="角色"
    )
    action = models.CharField(
        max_length=30,
        choices=action_choices,
        default="read",
        verbose_name="读写权限"
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="权限",
    )

    class Meta:
        db_table = "role_permission"
        app_label = USER_APP_LABEL
        unique_together = ("role",)
        verbose_name = "角色权限映射表"
