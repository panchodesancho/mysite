from django.contrib import admin
from shufic.models import Video, Comment





class VideoInline(admin.StackedInline):  # указывает связь
    model = Comment
    extra = 2  # колличество коментариев под статьей


class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_filter = ['Video_date']
    fields = ['Video_url','Video_title','Video_text']

admin.site.register(Video, VideoAdmin)