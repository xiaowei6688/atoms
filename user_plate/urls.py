# -*- coding: utf-8 -*-
"""
@File        : urls.py.py
@Author      : Lu Wei
@Time        : 2022/12/29 10:50 上午
@Description :
"""
from django.urls import path
from user_plate.views.user_operation import UserListCreateAPIView, UserLogin, Demos

urlpatterns = []
login = [
    path("system/users/", UserListCreateAPIView.as_view()),
    path("login/users/", UserLogin.as_view({"post": "login"})),
    path("qwe/", Demos.as_view()),
]


urlpatterns += login
