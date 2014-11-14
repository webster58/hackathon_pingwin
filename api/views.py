from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
# Create your views here.

import json

from django.http import HttpResponse

from hack.hack.models import Service
from django.views.decorators.http import require_http_methods
import subprocess

import pyping
import pxssh
import getpass
from django.views.decorators.csrf import csrf_exempt


def isInt(string):
    try:
        a = int(string)
        return True
    except: return False

def isFloat(string):
    try:
        a = float(string)
        return True
    except: return False


@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_test(request):
    data = {}
    data['result'] = 'failed'
    data['message'] = 'You messed up'
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def get_services(request):

    services = Service.objects.all()

    data = []

    for s in services:
        data.append({
            'name': s.name,
            'id': s.pk,
            'country': s.country,
            })

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def get_ping(request):

    _data = {}
    if request.method == "GET"
        _data = request.GET
    if request.method == "POST"
        _data = request.POST


    data = {}

    service = None
    if 'service' in _data:
        if isInt(_data['service']):
            service = Service.objects.get(pk = int(_data['service']))

    if service:
        data['service'] = service.name
        data['service_id'] = service.pk







    else:
        data['service'] = 'localhost'
        data['service_id'] = 0
        r = pyping.ping(_data["name"])

        data['ret_code'] = r.ret_code
        data['destination'] = r.destination
        data['max_rtt'] = r.max_rtt
        data['avg_rtt'] = r.avg_rtt
        data['min_rtt'] = r.min_rtt
        data['destination_ip'] = r.destination_ip

    return HttpResponse(json.dumps(data), content_type="application/json")