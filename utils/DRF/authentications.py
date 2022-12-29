# -*- coding: utf-8 -*-
"""
@File        : authentications.py
@Author      : Lu Wei
@Time        : 2022/12/29 5:21 下午
@Description :
"""
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, APIException

from utils.jwt_token import token_to_user_info
from user_plate.models.user import AtomUser


class LoginAuth(BaseAuthentication):

    def authenticate_header(self, request):
        """
        获取验证auth
        @param request:
        @return:
        """

        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if not auth:
            raise AuthenticationFailed('Login is required!')
        return auth

    def authenticate(self, request):
        # 拿token
        header, token = self.authenticate_header(request).split()
        # 去缓存看看有没有
        info = token_to_user_info(token)
        if not info:
            raise AuthenticationFailed('token不合法,请检查token值.')
        try:
            user = AtomUser.objects.get(pk=info.get("user_id"))
        except AtomUser.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        if (not user.is_active) or user.is_delete:
            raise AuthenticationFailed("该账户已被冻结")
        return user, token
