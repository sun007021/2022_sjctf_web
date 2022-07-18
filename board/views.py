from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import CommonBoard, PrivateBoard1, PrivateBoard2
from .forms import CommonBoardForm
from django.shortcuts import render, redirect
from django.utils import timezone
from users.decorators import login_message_required, check_user_able_to_see_page1, check_user_able_to_see_page2
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from users.models import User

def index(request):
    return render(request, 'board/index.html')

@method_decorator(login_message_required,name='dispatch')
class IndexView(ListView):# 공통 게시판
    def get_queryset(self):
        if self.request.user.groups.filter(name="세종대학교").exists(): # 세종대 즉 참가자의 경우 자신의 글만 보이도록함
            mypost = CommonBoard.objects.filter(writer=self.request.user)
            return mypost.order_by('-create_date')
        else: #참가자가 아닌경우 (ssg 크롤러)는 모든글을 볼 수 있도록함
            return CommonBoard.objects.order_by('-create_date')

@method_decorator(login_message_required,name='dispatch')
class DetailView(DetailView):
    model = CommonBoard
    def get(self, request, *args, **kwargs): # 자기글만 확인 가능
        if self.request.user.groups.filter(name="세종대학교").exists():
            self.object = self.get_object(queryset=CommonBoard.objects.filter(writer=self.request.user))
        return super().get(request, *args, **kwargs)

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
            commonboard.writer = request.user
            commonboard.save()
            return redirect('board:commonboard_list')
    else:
        form = CommonBoardForm()
    context = {'form': form}
    return render(request, 'board/commonboard_form.html', context)

