# -*- coding: utf-8 -*-
"""
@File        : model.py
@Author      : Lu Wei
@Time        : 2022/12/29 3:07 下午
@Description :
"""
import os
import pkgutil


def get_modules(app_name: str, file_path: str="."):
    """
    获取包名下所有非__init__的模块名
    :param app_name: app名字
    :param file_path: 包路径
    :return:
    """
    path = os.path.dirname(file_path)
    packages = pkgutil.walk_packages([path])
    for _, modname, __ in packages:
        exec(f'from {app_name}.models.' + modname + ' import *')
