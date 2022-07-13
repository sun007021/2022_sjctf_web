from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import CsRegisterForm
from django.views.generic import CreateView


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CsRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/board/index/')
    else:
        form = CsRegisterForm
    return render(request, 'users/register.html', {'form': form})