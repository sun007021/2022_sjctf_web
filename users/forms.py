from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class CsRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CsRegisterForm, self).save(commit=False)
        user.save()
        group = Group.objects.get(name='세종대학교')
        user.groups.add(group)
        return user
