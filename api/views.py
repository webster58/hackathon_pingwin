from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
# Create your views here.



def api_test(request):
    return {'api_test':'success'}
