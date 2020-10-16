import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    author = request.GET.get('author')
    print(author)
    text = request.GET.get('text')
    print(text)
    return HttpResponse(
        json.dumps({author: text}),
        content_type="application/json"
    )


@csrf_exempt
def create_post(request):
    author = request.GET.get('author')
    print(author)
    text = request.GET.get('text')
    print(text)
    return HttpResponse(
        json.dumps({author: text}),
        content_type="application/json"
    )


@csrf_exempt
def delete_post(request):
    author = request.GET.get('author')
    print(author)
    text = request.GET.get('text')
    print(text)
    return HttpResponse(
        json.dumps({author: text}),
        content_type="application/json"
    )
