# -*- coding: utf-8 -*-
"""
@File        : user_serializer.py
@Author      : Lu Wei
@Time        : 2022/12/29 3:35 下午
@Description :
"""
from django.db import transaction
from common.response import UserError
from rest_framework.exceptions import APIException
from rest_framework import serializers
from utils.phone import phone_validator
from rest_framework.serializers import ModelSerializer
from user_plate.models.user import AtomUser
from django.contrib.auth.hashers import make_password


class UserCreateSerializers(ModelSerializer):
    username = serializers.CharField(
    )
    nick_name = serializers.CharField(
        min_length=3,
        max_length=30,
    )
    password = serializers.CharField(
        write_only=True,
    )
    confirm_password = serializers.CharField(
        write_only=True,
    )
    email = serializers.EmailField()
    phone = serializers.CharField(
        max_length=11,
        min_length=11,
        validators=[phone_validator],
        trim_whitespace=True
    )

    def validate_email(self, value):
        # 校验邮箱是否存在
        value = value.strip()
        du_instance = AtomUser.objects.filter(email=value).exists()
        if du_instance:
            raise APIException(UserError.FAILED_EXISTS.value.format('邮箱'))
        return value

    def validate_phone(self, value):
        # 校验手机号
        value = value.strip()
        du_instance = AtomUser.objects.filter(phone=value).exists()
        if du_instance:
            raise APIException(UserError.FAILED_EXISTS.value.format('手机号'))
        return value

    @transaction.atomic
    def create(self, validated_data):
        username = validated_data.pop('username')
        nick_name = validated_data.pop('nick_name')
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        email = validated_data.pop('email')
        phone = validated_data.pop('phone')
        # 校验密码和确认密码
        if password.strip() != confirm_password.strip():
            raise APIException(UserError.CONFIRM_PASSWORD_ERROR.value)
        # 如果用户名存在
        if AtomUser.objects.filter(username=username).first():
            raise APIException(UserError.USER_EXISTS.value)
        user = AtomUser.objects.create(
            username=username,
            phone=phone,
            email=email,
            nick_name=nick_name,
            password=make_password(password),
        )
        return user

    class Meta:
        model = AtomUser
        fields = [
            'id', 'username', 'nick_name', 'email', 'phone',
            'date_joined', 'updated_at', 'password', 'confirm_password'
        ]
