from django.conf.urls import patterns, url
from navigate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^@(?P<xCoord>[0-9.-]+),(?P<yCoord>[0-9.-]+),z(?P<zoom>[0-9.-]+)/(?P<xSize>[0-9]+)/(?P<ySize>[0-9]+)/i(?P<iterations>[0-9]+)$', views.navigateTo, name='navigateTo'),
    url(r'^home/', views.home, name='home'),

# TODO regex params from url and pass to navigateTo

# ex: /polls/5/results/
# url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    )
