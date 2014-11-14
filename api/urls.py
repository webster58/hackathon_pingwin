from django.views.generic.base import TemplateView
from django.conf.urls import patterns, include, url

from api import views

urlpatterns = patterns('',
    url(r'^api_test^$', views.api_test, name='api_test'),
    url(r'^get_services/?', views.get_services, name='get_services'),
    url(r'^get_ping/?', views.get_ping, name='get_ping'),


  )