from django.conf.urls import url
from tech.views import *
from . import views
from tech.views import SSOLoginView

urlpatterns = [
    url(r'^$',SSOLoginView.as_view()),
    url(r'^login/', views.index, name='index'),
    url(r'^search/$', views.results, name='results'),
    url(r'^create/$', views.create, name='create'),

]

