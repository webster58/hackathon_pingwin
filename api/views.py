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
import re

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
    if request.method == "GET":
        _data = request.GET
    if request.method == "POST":
        _data = request.POST

    print "\n\n\n\n\n", request

    data = {}

    service = None
    if 'service' in _data:
        if isInt(_data['service']):
            if int(_data['service']) > 0:
                service = Service.objects.get(pk = int(_data['service']))
                if service.ip in ['localhost', '0.0.0.0', '127.0.0.0', 'localhost:8000', '0.0.0.0:8000', '127.0.0.0:8000']:
                    service = None

    if service:
        data['service'] = service.name
        data['service_id'] = service.pk


        s = pxssh.pxssh()

        if service.ssh_key_auth:

            if 'name' in _data:
                if not s.login ( service.ip, service.user, ssh_key = service.shhkey):
                    print "SSH session failed on login."
                    print str(s)
                else:
                    print "SSH session login successful"
                    s.sendline ('ping' + " -c 4 " + _data["name"])
                    s.prompt()         # match the prompt
                    raw_response_data = s.before
                    print s.before     # print everything before the prompt.
                    s.logout()

                    match = re.search('([\d]*\.[\d]*)/([\d]*\.[\d]*)/([\d]*\.[\d]*)/([\d]*\.[\d]*)', raw_response_data)

                    data['min_rtt'] = match.group(1)
                    data['avg_rtt'] = match.group(2)
                    data['max_rtt'] = match.group(3)

                    match = re.search('(d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', raw_response_data)
                    
                    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', raw_response_data )
                    if ip:
                        if len(ip):
                            data['destination_ip'] = ip[0]

                    data['ret_code'] = 0
                    data['destination'] = _data["name"]

    else:
        data['service'] = 'localhost'
        data['service_id'] = 0

        if 'name' in _data:
            if True:
                # r = pyping.ping(_data["name"])

                data['ret_code'] = "200"
                data['destination'] = "wp.pl"
                data['max_rtt'] = 200
                data['avg_rtt'] = 100
                data['min_rtt'] = 50
                data['destination_ip'] = "123.213.123.123"
            else:
                r = pyping.ping(_data["name"])

                data['ret_code'] = r.ret_code
                data['destination'] = r.destination
                data['max_rtt'] = r.max_rtt
                data['avg_rtt'] = r.avg_rtt
                data['min_rtt'] = r.min_rtt
                data['destination_ip'] = r.destination_ip
        else:
            data["error"] = "there is no <name> field in this request"

    return HttpResponse(json.dumps(data), content_type="application/json")