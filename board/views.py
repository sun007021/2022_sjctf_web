from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import CommonBoard
from .forms import CommonBoardForm
from django.shortcuts import render, redirect
from django.utils import timezone
from users.decorators import login_message_required

def index(request):
    return HttpResponse("안녕하세요 오신것을 환영합니다.")

class IndexView(ListView):
    def get_queryset(self):
        return CommonBoard.objects.order_by('-create_date')


class DetailView(DetailView):
    model = CommonBoard

@login_message_required
def commonboard_create(request):
    if request.method == 'POST':
        form = CommonBoardForm(request.POST)
        if form.is_valid():
            commonboard = form.save(commit=False)
            commonboard.create_date = timezone.now()
            commonboard.save()
            return redirect('board:commonboard_list')
    else:
        form = CommonBoardForm()
    context = {'form': form}
    return render(request, 'board/commonboard_form.html', context)

