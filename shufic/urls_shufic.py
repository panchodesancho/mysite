from django.urls import re_path
from shufic.views import Hello, onevideo, addlikes, addcomment, ajaxlike

urlpatterns = [
    re_path(r'^$', Hello),
    re_path(r'onevideo/(?P<video_id>\d+)/$', onevideo),
    re_path(r'addlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'addcomment/(?P<video_id>\d+)/$', addcomment),
    re_path(r'addlike/ajax/$', ajaxlike),
]