from django.conf.urls import url

from  . import views

from dream.views import *

urlpatterns = [
	url(r'^$',views.dash),
	url(r'^new/$',views.new),
	url(r'^search/$',views.text,name='sh'),
#	url(r'^car/$',views.car),
	url(r'^bar/$',views.bar),
	url(r'^repo/$',views.repo),
	url(r'^plat/$',views.plat),
	url(r'^image/$',views.image),
	url(r'^video/$',views.video),
	url(r'^carou/$',views.carou),
	url(r'^banner/$',views.banner),
	url(r'^map/$',views.map),
]
