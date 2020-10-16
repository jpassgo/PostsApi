import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return HttpResponse(
        'Home',
        content_type="application/json"
    )


@csrf_exempt
def create_post(request):
    print(request.body)
    body = json.loads(request.body)
    return HttpResponse(
        json.dumps({body['author']: body['text']}),
        content_type="application/json"
    )


@csrf_exempt
def delete_post(request):
    return HttpResponse(
        'delete',
        content_type="application/json"
    )
