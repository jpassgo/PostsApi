import json
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        json.dumps({{"PlaceHolderKey": "PlaceHolderValue"}}),
        content_type="application/json"
    )

def create_post(request):
    return HttpResponse(
        json.dumps({"PlaceHolderKey": "PlaceHolderValue"}),
        content_type="application/json"
    )

def delete_post(request):
    return HttpResponse(
        json.dumps({"PlaceHolderKey": "PlaceHolderValue"}),
        content_type="application/json"
    )