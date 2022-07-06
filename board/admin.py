from django.contrib import admin
from .models import CommonBoard, PrivateBoard1, PrivateBoard2
# class BoardAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'content',
#         'writer',
#         )
#     search_fields = ('title', 'content', 'writer__user_id',)

admin.site.register(CommonBoard)
admin.site.register(PrivateBoard1)
admin.site.register(PrivateBoard2)
