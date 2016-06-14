__author__ = 'Administrator'
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^calc/$', views.calc, name='calc'),
                       url(r'^user/$', views.user, name='user'),
                       )
