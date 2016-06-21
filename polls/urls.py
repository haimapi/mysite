__author__ = 'Jon'
from django.conf.urls import patterns, url
from polls import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
)