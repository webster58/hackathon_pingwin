from django.views.generic.base import TemplateView
from django.conf.urls import patterns, include, url

from hack.hack import views



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
  )