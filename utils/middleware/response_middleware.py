# -*- coding: utf-8 -*-
"""
@File        : response_middleware.py
@Author      : Lu Wei
@Time        : 2022/12/29 5:34 下午
@Description :
"""
import logging
import re

from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

ACCOUNT_LOGIN_FAILED_STATUS_CODE = 598

logger = logging.getLogger("response")


def flatten_response(data: dict):
    msg = []
    for k, v in data.items():
        if isinstance(v, list) and v:
            msg.append(v[0])
    return ", ".join(msg)


class ResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        """
        重写返回逻辑
        @param request:
        @param response:
        @return:
        """
        resp = {}
        if isinstance(response, Response):
            if str(response.status_code)[:1] == "2":
                data = response.data
                if data is None:
                    data = {}
                if isinstance(data, list):
                    resp["code"] = status.HTTP_200_OK
                    resp["msg"] = "ok"
                    resp["data"] = data
                    response.data = resp
                    response._is_rendered = False
                    response.render()
                    return response
                code = status.HTTP_200_OK
                msg = "ok"
                if "code" in data:
                    code = data.pop("code")
                if "msg" in data:
                    msg = data.pop("msg")
                resp["code"] = code
                resp["msg"] = msg
                if "data" in data.keys() and len(data.keys()) == 1:
                    resp["data"] = data.pop("data")
                else:
                    resp["data"] = data
                response.data = resp
            elif response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
                resp["code"] = response.data.get("code", status.HTTP_500_INTERNAL_SERVER_ERROR)
                resp["msg"] = response.data.get("detail", "")
                resp["data"] = None
                response.data = resp
            elif response.status_code == status.HTTP_400_BAD_REQUEST:
                resp["code"] = response.status_code
                resp["msg"] = f"参数缺失或不符合规范，请检查输入内容。 {flatten_response(response.data)}"
                resp["data"] = None
                response.data = resp
            elif response.status_code == status.HTTP_401_UNAUTHORIZED:
                resp["code"] = response.status_code
                resp["msg"] = response.data.get("detail")
                resp["data"] = None
                response.data = resp
            elif response.status_code == status.HTTP_403_FORBIDDEN:
                resp["code"] = response.status_code
                resp["msg"] = "暂无权限，请联系管理员。"
                resp["data"] = None
                response.data = resp
            elif response.status_code == status.HTTP_404_NOT_FOUND:
                resp["code"] = response.status_code
                resp["msg"] = response.data.get("detail", "not found")
                resp["data"] = None
                response.data = resp
            elif response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
                resp["code"] = response.status_code
                resp["msg"] = response.data.get("detail", "method not allowed")
                resp["data"] = None
                response.data = resp
            elif response.status_code == status.HTTP_406_NOT_ACCEPTABLE:
                msg = response.data.get("detail", "")
                resp["code"] = response.status_code
                resp["msg"] = msg if msg else f"参数缺失或不符合规范，请检查 {response.data}"
                resp["data"] = None
                response.data = resp
            elif response.status_code == ACCOUNT_LOGIN_FAILED_STATUS_CODE:
                msg = response.data.get("detail", "")
                resp["code"] = response.status_code
                resp["msg"] = msg if msg else f"参数缺失或不符合规范，请检查 {response.data}"
                resp["data"] = None
                response.data = resp
            else:
                resp["code"] = response.status_code
                resp["msg"] = "后端走神儿了，请稍后再试"
                resp["data"] = None
                response.data = resp
            response.status_code = status.HTTP_200_OK
            response._is_rendered = False
            response.render()
        return response

    def process_exception(self, request, exception):
        """
        捕捉异常
        @param request:
        @param exception:
        @return:
        """
        resp = {}
        if isinstance(exception, AuthenticationFailed):
            resp["code"] = status.HTTP_401_UNAUTHORIZED
            resp["msg"] = "请登录"
        elif isinstance(exception, IntegrityError):
            pattern = re.compile(r"=\((.*?)\) already exists")
            result = pattern.search(str(exception))
            if result:
                repeat_field = result.group(1).split(",")[-1]
                resp["code"] = status.HTTP_406_NOT_ACCEPTABLE
                resp["msg"] = f"{repeat_field} 已存在！"
            else:
                resp["code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
                resp["msg"] = f"后端拥挤，请稍后再试:{str(exception)}"
        else:
            resp["code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            resp["msg"] = f"后端拥挤，请稍后再试:{str(exception)}"
        resp["data"] = None
        logger.error(exception)
        response = JsonResponse(data=resp, status=status.HTTP_200_OK)
        return response
