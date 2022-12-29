# -*- coding: utf-8 -*-
"""
@File        : __init__.py.py
@Author      : Lu Wei
@Time        : 2022/12/29 2:32 下午
@Description :
"""
from utils.model import get_modules


# 挂载模型文件内的model
get_modules("user_plate", __file__)
