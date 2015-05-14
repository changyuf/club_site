from django.conf.urls import patterns, url

from club_admin import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)