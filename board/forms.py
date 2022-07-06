from django import forms
from board.models import CommonBoard


class CommonBoardForm(forms.ModelForm):
    class Meta:
        model = CommonBoard  # 사용할 모델
        fields = ['title', 'content']
