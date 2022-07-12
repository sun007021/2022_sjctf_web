from django import template
from django.contrib.auth.models import Group
import re
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False

@register.filter(name='protect_xss')
def protect_xss(value):
    content = value.content #전달 받은 value 객체의 content 멤버변수를 가져옴
    #tags = value.tag_set.all() # 전달된 객체의 tag_set 전체를 가져오는 queryset을 리턴

    #for tag in tags: # tags의 각각의 인스턴트 순회하며 content에서 해당 문자열을 replace
    content = re.sub(r'script|img|noscript|javascript|SCRIPT|onload|frame', '', content)
    return content