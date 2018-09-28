from django.urls import re_path
from loginout.log_views import login, logout


urlpatterns = [
    re_path(r'in/$', login),
    re_path(r'out/$', logout),
]