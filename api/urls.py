from django.views.generic.base import TemplateView
from django.conf.urls import patterns, include, url

from api import views



urlpatterns = patterns('',
    url(r'api_test^$', views.api_test, name='api_test'),
  )