__author__ = 'Administrator'
from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^read/(?P<slug_title>[\w\-]+)/$', views.view_blog, name='view_blog'),
)