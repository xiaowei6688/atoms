from django.shortcuts import render
import logging
import datetime
from django.core.cache import cache
from utils.jwt_token import token_to_user_info, user_info_to_token
from user_plate.models.user import AtomUser
from rest_framework.exceptions import APIException
from user_plate.serializer.user_serializer import UserCreateSerializers
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from common.response import RegisterResponse, LoginResponse

logger = logging.getLogger('user_plate')


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserCreateSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "code": status.HTTP_200_OK,
            "msg": RegisterResponse.SUCCESS
        })


class UserLogin(ViewSet):

    @action(detail=False)
    def login(self, request):
        data = request.data
        phone = data.get("phone")
        try:
            # 没有被主系统停用的用户
            user = AtomUser.objects.get(phone=phone, is_active=True)
        except AtomUser.DoesNotExist:
            logger.error(f'not found phone: {phone} ')
            raise APIException(LoginResponse.USERINFO_ERROR.value)

        if not user.check_password(data.get("password")):
            logger.error(f'uname or pwd error')
            raise APIException(LoginResponse.USERINFO_ERROR.value)

        # 生成token
        token = user_info_to_token({"user_id": user.id})
        # 通过filter的update方法不经过model层，因此不会更新用户的更新时间
        AtomUser.objects.filter(id=user.id).update(last_login=datetime.datetime.now())
        resp = {
            'id': user.pk,
            "token": token,
            "username": user.username,
            "phone": user.phone,
            "nick_name": user.nick_name,
        }
        return Response(resp)


class Demos(ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        return Response({"code": 200})
