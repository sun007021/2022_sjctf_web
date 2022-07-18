# notice/models.py

import os
from django.conf import settings
from django.db import models
from users.models import User
import datetime

class CommonBoard(models.Model): #공통 게시판
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.CharField(max_length=256, verbose_name='내용')
    create_date = models.DateTimeField(null=True, blank=False)

class PrivateBoard1(models.Model): #비밀1 게시판
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.CharField(max_length=128, verbose_name='제목')
    create_date = models.DateTimeField(null=True, blank=False)

class PrivateBoard2(models.Model): #공통 게시판
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(null=True, blank=False)