# notice/models.py

import os
from django.conf import settings
from django.db import models

class Board(models.Model): #공통 게시판
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')

    def __str__(self):
        return self.title

    class Meta:
        db_table = '공통게시판'
        verbose_name = '공통게시판'
        verbose_name_plural = '공통게시판'