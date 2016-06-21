from django.conf.urls import patterns, include, url
from django.contrib import admin
import rango

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^blog/',  include('blog.urls')),
    url(r'^news/',  include('news.urls')),
    url(r'^polls/', include('polls.urls')),
)
