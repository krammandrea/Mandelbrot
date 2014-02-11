from django.conf.urls import patterns, url
from navigate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),

# ex: /polls/5/results/
# url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    )
