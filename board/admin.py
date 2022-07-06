from django.contrib import admin
from .models import CommonBoard
# class BoardAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'content',
#         'writer',
#         )
#     search_fields = ('title', 'content', 'writer__user_id',)

admin.site.register(CommonBoard)
