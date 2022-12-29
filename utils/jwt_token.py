# -*- coding: utf-8 -*-
"""
@File        : jwt_token.py
@Author      : Lu Wei
@Time        : 2022/12/29 4:57 下午
@Description :
"""
from typing import Union
import jwt
from jwt.exceptions import DecodeError
from datetime import datetime, timedelta
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY


def user_info_to_token(user_info: dict, expire_days: int = 30) -> str:
    """
    获取jwt token
    :param user_info: 用户信息
    :param expire_days: 过期天数，默认一天
    :return: jwt token
    """
    # 不修改输入, 重新赋值
    token_info = {key: user_info[key] for key in user_info}
    # 设置过期时间
    if "expire_time" not in token_info:
        token_info["expire_time"] = str(datetime.now() + timedelta(days=expire_days))
    encoded_jwt = jwt.encode(token_info, SECRET_KEY, algorithm='HS256')
    return encoded_jwt


def token_to_user_info(token: str) -> Union[dict, None]:
    """
    jwt token 转成user信息
    :param token: jwt token
    :return: 用户信息或None
    """
    try:
        user_info = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except DecodeError:
        return None
    if not user_info or "expire_time" not in user_info:
        return None
    expire_time = datetime.strptime(user_info["expire_time"].split(".")[0], '%Y-%m-%d %H:%M:%S')
    # 判断是否过期
    if (expire_time - datetime.now()).total_seconds() < 0:
        return None
    user_info.pop("expire_time")
    return user_info
