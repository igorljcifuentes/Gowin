from django.conf.urls import patterns, include, url
from django.contrib import admin

from gowin import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'encuesta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
