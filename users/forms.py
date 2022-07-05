from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm


class CsRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super(CsRegisterForm, self).save(commit=False)
    #     user.level = '2'
    #     user.groups = '세종대학교'
    #     user.save()
    #     return user
