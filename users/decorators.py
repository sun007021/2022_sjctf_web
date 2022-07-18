from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from users.models import User
from django.http import HttpResponse


# 로그인 확인
def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
        return function(request, *args, **kwargs)
    return wrap


# 관리자 권한 확인
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.usetr.level == '1' or request.user.level == '0':
            return function(request, *args, **kwargs)
        messages.warning(request, "접근 권한이 없습니다.")
        return redirect('/users/main/')
    return wrap


# 비로그인 확인
def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            return redirect('/users/main/')
        return function(request, *args, **kwargs)
    return wrap

# group1 확인
def check_user_able_to_see_page1(function):
    def wrap(request, *args, **kwargs):
        if request.user.groups.filter(name="세종대학교").exists():
            return function(request, *args, **kwargs)
        else:
            messages.warning(request, "세종대학교 학생만 이용가능합니다.")
        return redirect('/board/commonboard')

    return wrap

# group2 확인
def check_user_able_to_see_page2(function):
    def wrap(request, *args, **kwargs):
        if request.user.groups.filter(name="SSG대학교").exists():
            return function(request, *args, **kwargs)
        else:
            messages.warning(request, "SSG대학교 학생만 이용가능합니다.")
        return redirect('/board/commonboard')

    return wrap
