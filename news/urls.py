__author__ = 'jon'
from django.conf.urls import url, patterns
import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)