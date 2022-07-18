from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import CommonBoard, PrivateBoard1, PrivateBoard2
from .forms import CommonBoardForm
from django.shortcuts import render, redirect
from django.utils import timezone
from users.decorators import login_message_required, check_user_able_to_see_page1, check_user_able_to_see_page2
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

def index(request):
    return render(request, 'board/index.html')

@method_decorator(login_message_required,name='dispatch')
class IndexView(ListView):# 공통 게시판
    def get_queryset(self):
        return CommonBoard.objects.order_by('-create_date')


class DetailView(DetailView):
    model = CommonBoard

# @login_message_required

@method_decorator(check_user_able_to_see_page1, name='dispatch')
class IndexViewP1(ListView):#비밀 게시판1
    def get_queryset(self):
        return PrivateBoard1.objects.order_by('-create_date')

@method_decorator(check_user_able_to_see_page1, name='dispatch')
class DetailViewP1(DetailView):
    model = PrivateBoard1


@method_decorator(check_user_able_to_see_page2, name='dispatch')
class IndexViewP2(ListView):#비밀 게시판2
    def get_queryset(self):
        return PrivateBoard2.objects.order_by('-create_date')

@method_decorator(check_user_able_to_see_page2, name='dispatch')
class DetailViewP2(DetailView):
    model = PrivateBoard2

@login_message_required
def commonboard_create(request):
    if request.method == 'POST':
        form = CommonBoardForm(request.POST)
        if form.is_valid():
            commonboard = form.save(commit=False)
            commonboard.create_date = timezone.now()
            session_id = request.session.get('sessionid')
            user = User.objects.get(user_id= session_id)
            commonboard.writer = user
            commonboard.save()
            return redirect('board:commonboard_list')
    else:
        form = CommonBoardForm()
    context = {'form': form}
    return render(request, 'board/commonboard_form.html', context)

