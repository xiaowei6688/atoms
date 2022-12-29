# -*- coding: utf-8 -*-
"""
@File        : phone.py
@Author      : Lu Wei
@Time        : 2022/12/29 3:40 下午
@Description :
"""
import re
from rest_framework.serializers import ValidationError


def phone_validator(phone: str) -> str:
    """
    手机号验证
    @param phone:
    @return:
    """
    ret = re.match(r"^1[3456789]\d{9}$", phone)
    if ret:
        return phone
    raise ValidationError("手机号不合法")


def identifier_validator(string):
    """
    检验用于变量的标识符
    @param string:
    @return:
    """
    regex = r'^[A-Za-z_][A-Za-z0-9_]*$'
    ret = re.match(regex, string)
    if ret:
        return string
    raise ValidationError("标识符不合法")
