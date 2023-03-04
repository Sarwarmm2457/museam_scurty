from django.urls import path
from . import views
from django.urls import re_path as url 
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='home'),
    path('login', views.login_view, name='login'),
    path('second_auth', views.secondAuth, name='auth')
]