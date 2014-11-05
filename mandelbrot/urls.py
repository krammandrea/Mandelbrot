from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('navigate.urls')),
    url(r'^navigate/', include('navigate.urls')),
    )

urlpatterns += staticfiles_urlpatterns()
